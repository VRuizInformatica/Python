# ──────────────────────────  Imports  ──────────────────────────
from datetime import datetime, timedelta         # date utilities
import pandas as pd                              # DataFrame handling
from fastapi.responses import JSONResponse       # JSON response helper


# ───────────────────  Endpoint: GET /securitization-information  ───────────────────
@PSummaryRouter.get("/securitization-information")
async def get_securitization_information():
    """
    Return PAYMENT_TYPE (English), Next Payment Date and Cut-Off Date
    for every record in the SECURITIZATION table.
    Assumes all fields are present and consistent.
    """

    # 1️⃣ Load the necessary columns from Oracle
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

    today = datetime.today().date()              # common cut-off date

    # Fixed day count by payment type (all values already in English)
    DAYS_BY_TYPE = {
        "weekly":        7,
        "biweekly":     15,
        "monthly":      30,
        "quarterly":    90,
        "four-monthly":120,
        "semi-annual": 180,
        "annual":      365,
        "balloon":       None,
    }

    # 2️⃣ Compute the next payment date for each row
    def _next_payment(row):
        ptype = row["PAYMENT_TYPE"].strip().lower()

        if ptype == "balloon":
            # For Balloon, return maturity date directly
            return row["SCH_MATURITY_DATE"].strftime("%d/%m/%Y")

        expected_days = DAYS_BY_TYPE[ptype]      # assume always present
        first = row["FIRST_PAYMENT_DATE"]

        next_date = first
        while next_date <= today:                # advance until after today
            next_date += timedelta(days=expected_days)

        return next_date.strftime("%d/%m/%Y")

    df["Next Payment Date"] = df.apply(_next_payment, axis=1)

    # 3️⃣ Add the cut-off date column
    df["Cut-Off Date"] = today.strftime("%d/%m/%Y")

    # 4️⃣ Return the results as JSON
    return JSONResponse(content=df.to_dict(orient="records"))
