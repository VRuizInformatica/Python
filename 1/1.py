# ────────────────────────────────────────────────────────────────────────────────
# Datos transversales
# ────────────────────────────────────────────────────────────────────────────────
@PManagementRouter.get("/general-data", tags=["general"])
async def get_general_data():
    """Devuelve la fecha de corte más reciente para toda la herramienta."""
    row = helper_oracle.load_data(
        "CONTRACT",
        columns=["MAX(DATA_CUT_OFF_DATE) AS last_reference_date"]
    )[0]
    return { "last_reference_date": row["last_reference_date"] }
