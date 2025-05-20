@router.get("/manual-removals")
async def get_manual_removals(loanIdentifier: str = Query(None, description="Filtrar por Loan Identifier")):
    """
    Este endpoint carga los activos de la pestaña "pm-1" del Excel PORTFOLIO_MANAGEMENT,
    ubicado en securization-front>data>PORTFOLIO_MANAGEMENT.
   
    Se filtran únicamente los activos que estén titulizados (con la marca "securitized") y
    opcionalmente se filtra por Loan Identifier.
   
    Para cada activo se añaden manualmente los siguientes campos:
    - STATUS
    - Reason
    - Date of Inclusion
    - Date of Exclusion
 
    Se devuelve un JSON con el formato
    {
    "Loan Identifier": "17066640",
    "STATUS": "proposed",
    "Weighted Average Interest Rate": "0.843392663930723",
    "Interest Mean": "150",
    "Interest Rate Index": "0.01",
    "Maturity Date": "2028-08-05 00:00:00",
    "Verification Agent Validation": "Approved",
    "Cost": "1003",
    "Reason": "Annual interest rate decreased for over 10% of portfolio assets.",
    "Date of Inclusion": "2025-03-24",
    "Date of Exclusion": null,
    "Current Principal Outstanding Balance": "250000"
    }.
    """
    try:
        # Cargar los datos desde el Excel (PORTFOLIO_MANAGEMENTpestaña "pm-1")
        df = helper_excel.load_data("data/PORTFOLIO_MANAGEMENT.xlsx", "pm-1")
       
        # Filtrar los activos titulizados "securitized"
        if "securitized" in df.columns:
            df = df[df["securitized"].str.lower() == "securitized"]
        else:
            raise HTTPException(status_code=500, detail="No se encontró la columna 'securitized' para filtrar los  activos.")
 
        # Filtrar por el Loan Identifier si se proporciona
        if loanIdentifier:
            df = df[df["Loan Identifier"].astype(str) == loanIdentifier]
       
        # Añadir o sobrescribir los campos manuales requeridos
        df["STATUS"] = "manual proposed"
        df["Reason"] = "Manual added by Verification Agent"
        today_date = datetime.today().strftime("%Y-%m-%d")
        df["Date of Inclusion"] = today_date
        df["Date of Exclusion"] = None
 
        # Selecciona solo las columnas pedidas
        required_columns = [
            "Loan Identifier",
            "STATUS",
            "Weighted Average Interest Rate",
            "Interest Mean",
            "Interest Rate Index",
            "Maturity Date",
            "Verification Agent Validation",
            "Cost",
            "Reason",
            "Date of Inclusion",
            "Date of Exclusion",
            "Current Principal Outstanding Balance"
        ]
        existing_columns = [col for col in required_columns if col in df.columns]
        df = df[existing_columns]
       
        data = df.to_dict(orient="records")
        return JSONResponse(content=data)
   
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error procesand manual removals: {e}")
