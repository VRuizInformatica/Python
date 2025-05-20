from fastapi import HTTPException, Query
from fastapi.responses import JSONResponse
from datetime import datetime
import pandas as pd

# ――― PManagementRouter ya debe estar importado arriba ――― #

@PManagementRouter.get("/manual-removals")
async def get_manual_removals(
    loanIdentifier: str = Query(
        default=None,
        description="Filtra por Loan Identifier (exacto)"
    )
):
    """
    Devuelve los activos “manual removals” a partir de la pestaña *pm-1*
    de PORTFOLIO_MANAGEMENT.xlsx, sólo los titulizados y
    opcionalmente filtrados por Loan Identifier.
    """
    try:
        # 1. Cargar el Excel
        df: pd.DataFrame = helper_excel.load_data(
            "data/PORTFOLIO_MANAGEMENT.xlsx",
            sheet_name="pm-1"
        )

        # 2. Filtrar por columna 'securitized'
        if "securitized" not in df.columns:
            raise HTTPException(
                status_code=500,
                detail="No se encontró la columna 'securitized' para filtrar los activos."
            )

        df = df[df["securitized"].str.lower() == "securitized"]

        # 3. Filtrar por Loan Identifier (si llega)
        if loanIdentifier:
            df = df[df["Loan Identifier"].astype(str) == loanIdentifier]

        # 4. Añadir/actualizar campos manuales
        today_str = datetime.today().strftime("%Y-%m-%d")
        df["STATUS"] = "manual proposed"
        df["Reason"] = "Manual added by Verification Agent"
        df["Date of Inclusion"] = today_str
        df["Date of Exclusion"] = None  # se deja explícitamente como null

        # 5. Seleccionar columnas finales
        required_cols = [
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
            "Current Principal Outstanding Balance",
        ]
        df = df[[c for c in required_cols if c in df.columns]]

        # 6. Responder
        return JSONResponse(content=df.to_dict(orient="records"))

    except HTTPException:
        # Re-lanzamos tal cual si ya es HTTPException
        raise
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Error procesando manual removals: {exc}"
        ) from exc
