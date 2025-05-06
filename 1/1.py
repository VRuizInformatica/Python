@PSummaryRouter.get("/securitization-information")
async def get_securitization_information():
    """
    Lee la tabla SECURITIZATION y devuelve, para cada titulización,
    la fecha del próximo pago (‘Next Payment Date’) y la fecha de corte
    (‘Cut-Off Date’).  
    • “Next Payment Date” se calcula en función de FIRST_PAYMENT_DATE,
    PAYMENT_TYPE y PAYMENT_FREQUENCY.  
    • Si PAYMENT_TYPE = 'Balloon' devolvemos SCH_MATURITY_DATE.  
    • Si PAYMENT_FREQUENCY no coincide con el tipo, devolvemos 400.
    """

    # 1️⃣ Leer los datos que realmente necesitamos
    df = helper_oracle.load_data(
        """
        SELECT
            SEC_ID,
            FIRST_PAYMENT_DATE,
            PAYMENT_TYPE,
            PAYMENT_FREQUENCY,
            SCH_MATURITY_DATE
        FROM   SECURITIZATION
        """,
        as_dataframe=True,
    )

    # 2️⃣ Fecha de corte (hoy) en formato dd/MM/yyyy
    today_date     = datetime.today().date()
    today_str      = today_date.strftime("%d/%m/%Y")

    # 3️⃣ Equivalencia: tipo de pago → número fijo de días
    TYPE_TO_DAYS = {
        "semanal":        7,
        "quincenal":     15,
        "mensual":       30,
        "trimestral":    90,
        "cuatrimestral":120,
        "semestral":    180,
        "anual":        365,
        # 'balloon' se controla aparte
    }

    # 4️⃣ Función que calcula el próximo pago para una fila
    def _calc_next_payment(row):
        sec_id = row["SEC_ID"]                         # para mensajes de error
        ptype  = str(row["PAYMENT_TYPE"]).strip().lower()
        freq   = row["PAYMENT_FREQUENCY"]

        # Caso especial: Balloon → usar la fecha de madurez tal cual
        if ptype == "balloon":
            maturity = row["SCH_MATURITY_DATE"]
            if pd.isna(maturity):
                raise ValueError(f"SEC_ID {sec_id}: SCH_MATURITY_DATE vacío")
            return maturity.strftime("%d/%m/%Y")

        # 4.a Validar que conocemos el tipo
        if ptype not in TYPE_TO_DAYS:
            raise ValueError(f"SEC_ID {sec_id}: PAYMENT_TYPE desconocido «{row['PAYMENT_TYPE']}»")

        expected_days = TYPE_TO_DAYS[ptype]

        # 4.b Validar coincidencia tipo ↔ frecuencia
        if pd.isna(freq) or int(freq) != expected_days:
            raise ValueError(
                f"SEC_ID {sec_id}: PAYMENT_FREQUENCY={freq} (no coincide con {expected_days} días para «{row['PAYMENT_TYPE']}»)"
            )

        # 4.c Calcular siguiente fecha a partir del primer pago
        first = row["FIRST_PAYMENT_DATE"]
        if pd.isna(first):
            raise ValueError(f"SEC_ID {sec_id}: FIRST_PAYMENT_DATE vacío")

        next_date = first
        while next_date <= today_date:
            next_date += timedelta(days=expected_days)

        return next_date.strftime("%d/%m/%Y")          # dd/MM/yyyy

    # 5️⃣ Aplicar el cálculo con control de errores profesionales
    try:
        df["Next Payment Date"] = df.apply(_calc_next_payment, axis=1)
    except ValueError as exc:
        # Cualquier incoherencia devuelve 400 con mensaje claro
        raise HTTPException(status_code=400, detail=str(exc))

    # 6️⃣ Añadir la fecha de corte (igual para todas las filas)
    df["Cut-Off Date"] = today_str

    # 7️⃣ DataFrame → lista de diccionarios y enviar como JSON
    return JSONResponse(content=df.to_dict(orient="records"))
