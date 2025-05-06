@PSummaryRouter.get("/securitization-information")
async def get_securitization_information():
    """
    Read the `securitization` table, ensure `payment_type` and
    `payment_frequency` are coherent, and return:
        • payment_type  (English only)
        • Next Payment Date
        • Cut-Off Date (today)
    """

    # 1️⃣ Pull only the columns we really need — helper_oracle is unchanged
    df = helper_oracle.load_data(
        table_name="securitization",
        columns=[
            "sec_id",
            "first_payment_date",
            "payment_type",        # assumed to be in English already
            "payment_frequency",
            "sch_maturity_date",
        ],
        mapping=SecuritizationInformationMapping,
    )

    today = datetime.today().date()               # cut-off date for every row

    # payment_type → expected number of days (Balloon handled separately)
    DAYS_BY_TYPE = {
        "weekly":         7,
        "biweekly":      15,
        "monthly":       30,
        "quarterly":     90,
        "four-monthly": 120,
        "semi-annual":  180,
        "annual":       365,
        "balloon":       None,
    }

    def _next_payment(row):
        """Validate one row and compute its next payment date."""
        sec_id   = row["sec_id"]
        ptype    = str(row["payment_type"]).strip().lower()

        # -- validation: payment_type must be recognised
        if ptype not in DAYS_BY_TYPE:
            raise ValueError(f"SEC_ID {sec_id}: unknown payment_type '{row['payment_type']}'")

        expected_days = DAYS_BY_TYPE[ptype]

        # -- Balloon: simply return the maturity date
        if ptype == "balloon":
            maturity = row["sch_maturity_date"]
            # -- validation: maturity date must exist
            if pd.isna(maturity):
                raise ValueError(f"SEC_ID {sec_id}: sch_maturity_date is NULL for Balloon")
            return maturity.strftime("%d/%m/%Y")

        # -- validation: numeric frequency must match the expected value
        freq = row["payment_frequency"]
        if pd.isna(freq) or int(freq) != expected_days:
            raise ValueError(
                f"SEC_ID {sec_id}: payment_frequency={freq} ≠ {expected_days} days for '{ptype.title()}'"
            )

        # -- validation: first_payment_date must not be null
        first = row["first_payment_date"]
        if pd.isna(first):
            raise ValueError(f"SEC_ID {sec_id}: first_payment_date is NULL")

        # compute the first payment date strictly after today
        next_date = first
        while next_date <= today:
            next_date += timedelta(days=expected_days)
        return next_date.strftime("%d/%m/%Y")

    # 2️⃣ Apply the calculation and turn any incoherence into HTTP 422
    try:
        df["Next Payment Date"] = df.apply(_next_payment, axis=1)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(exc),
        )

    # 3️⃣ Add the cut-off date column (identical for every row)
    df["Cut-Off Date"] = today.strftime("%d/%m/%Y")

    # 4️⃣ Return the DataFrame as a list of dicts
    return JSONResponse(content=df.to_dict(orient="records"))
