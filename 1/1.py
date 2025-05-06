# ─────────────── Imports ───────────────
from datetime import datetime, timedelta
import pandas as pd
from fastapi.responses import JSONResponse


@PSummaryRouter.get("/securitization-information")
async def get_securitization_information():
    """
    Returns PAYMENT_TYPE (English), Next Payment Date and Cut-Off Date
    for every record in SECURITIZATION.
    """

    # 1️⃣  Fetch required columns via helper_oracle.load_data
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

    today_date = datetime.today().date()
    today_str  = today_date.strftime("%d/%m/%Y")

    # Fixed day count by type
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

    # 2️⃣  Row-level calculation
    def calc_next_payment(row):
        ptype = row["PAYMENT_TYPE"].strip().lower()

        if ptype == "balloon":
            return row["SCH_MATURITY_DATE"].strftime("%d/%m/%Y")

        step_days = DAYS_BY_TYPE[ptype]              # always present
        next_date = row["FIRST_PAYMENT_DATE"]

        while next_date <= today_date:
            next_date += timedelta(days=step_days)

        return next_date.strftime("%d/%m/%Y")

    df["Next Payment Date"] = df.apply(calc_next_payment, axis=1)

    # 3️⃣  Common cut-off date
    df["Cut-Off Date"] = today_str

    # 4️⃣  JSON response
    return JSONResponse(content=df.to_dict(orient="records"))
