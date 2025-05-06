# ──────────────────────────  Imports  ──────────────────────────
from datetime import datetime, timedelta          # date utilities
import pandas as pd                               # DataFrame handling
from fastapi import HTTPException, status         # FastAPI errors
from fastapi.responses import JSONResponse        # JSON responses


# ────────────────────  Endpoint: GET /securitization-information  ────────────────────
@PSummaryRouter.get("/securitization-information")
async def get_securitization_information():
    """
    Read the `SECURITIZATION` table, verify that `PAYMENT_TYPE`
    and `PAYMENT_FREQUENCY` are consistent, and return:
        • PAYMENT_TYPE        (English label)
        • Next Payment Date   (dd/MM/yyyy)
        • Cut-Off Date        (today, dd/MM/yyyy)
    """

    # 1️⃣  Load only the columns we need (helper_oracle signature respected)
    df = helper_oracle.load_data(
        table_name="SECURITIZATION",
        columns=[
            "SEC_ID",
            "FIRST_PAYMENT_DATE",
            "PAYMENT_TYPE",
            "PAYMENT_FREQUENCY",
            "SCH_MATURITY_DATE",
        ],
    )

    today = datetime.today().date()               # common cut-off date

    # PAYMENT_TYPE → expected number of days (Balloon handled separately)
    DAYS_BY_TYPE = {
        "weekly":         7,
        "biweekly":      15,
        "monthly":       30,
        "quarterly":     90,
        "four-monthly": 120,
        "semi-annual":  180,
        "annual":       365,
        "balloon":        None,
    }

    # ─────────────────────  Helper for each row  ─────────────────────
    def _next_payment(row):
        """Validate one row and compute its next payment date."""
        sec_id = row["SEC_ID"]
        ptype  = str(row["PAYMENT_TYPE"]).strip().lower()

        # -- validation: payment_type must be recognised
        if ptype not in DAYS_BY_TYPE:
            raise ValueError(f"SEC_ID {sec_id}: unknown PAYMENT_TYPE '{row['PAYMENT_TYPE']}'")

        expected_days = DAYS_BY_TYPE[ptype]

        # -- Balloon: simply return maturity date
        if ptype == "balloon":
            maturity = row["SCH_MATURITY_DATE"]
            # -- validation: maturity date must exist
            if pd.isna(maturity):
                raise ValueError(f"SEC_ID {sec_id}: SCH_MATURITY_DATE is NULL for Balloon")
            return maturity.strftime("%d/%m/%Y")

        # -- validation: numeric frequency must match expected days
        freq = row["PAYMENT_FREQUENCY"]
        if pd.isna(freq) or int(freq) != expected_days:
            raise ValueError(
                f"SEC_ID {sec_id}: PAYMENT_FREQUENCY={freq} ≠ {expected_days} days for '{ptype.title()}'"
            )

        # -- validation: FIRST_PAYMENT_DATE must exist
        first = row["FIRST_PAYMENT_DATE"]
        if pd.isna(first):
            raise ValueError(f"SEC_ID {sec_id}: FIRST_PAYMENT_DATE is NULL")

        # compute the first payment date strictly after today
        next_date = first
        while next_date <= today:
            next_date += timedelta(days=expected_days)
        return next_date.strftime("%d/%m/%Y")

    # 2️⃣  Apply the calculation; any inconsistency ➜ HTTP 422
    try:
        df["Next Payment Date"] = df.apply(_next_payment, axis=1)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(exc),
        )

    # 3️⃣  Add the cut-off date column (same value for every row)
    df["Cut-Off Date"] = today.strftime("%d/%m/%Y")

    # 4️⃣  Return the DataFrame as JSON
    return JSONResponse(content=df.to_dict(orient="records"))
