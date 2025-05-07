# ─────────────── Imports ───────────────
from datetime import datetime, timedelta
import pandas as pd
from fastapi.responses import JSONResponse


@PSummaryRouter.get("/securitization-information")
async def get_securitization_information():
    """
    Returns PAYMENT_TYPE (as stored), Next Payment Date and Cut-Off Date
    for every record in SECURITIZATION.

    • El único PAYMENT_TYPE relevante es «quatrimestral».
    • La lógica de pago es: día 28 de febrero, mayo, agosto y noviembre,
      ajustado a Día Hábil (no fin de semana):
        – si el 28 es sábado/domingo → siguiente día hábil;
        – si al avanzar se entra en el mes siguiente → retroceder al
          día hábil inmediatamente anterior al 28.
    • Hasta que exista calendario de festivos sólo se excluyen fines de semana.
    """

    # 1️⃣  Cargamos los campos necesarios con el helper ORIGINAL
    df = helper_oracle.load_data(
        table_name="SECURITIZATION",
        columns=[
            "SEC_ID",
            "FIRST_PAYMENT_DATE",
            "PAYMENT_TYPE",
        ],
    )

    today_date = datetime.today().date()
    today_str  = today_date.strftime("%d/%m/%Y")

    QUARTER_MONTHS = (2, 5, 8, 11)     # Feb, May, Aug, Nov
    TARGET_DAY     = 28                # día 28 del mes

    # ─── función de ajuste a Día Hábil según la regla dada ───
    def adjust_to_business_day(base_date: datetime.date) -> datetime.date:
        """
        • Avanza al siguiente weekday si el 28 cae en fin de semana.
        • Si eso desborda al mes siguiente, retrocede al weekday anterior.
        """
        candidate = base_date
        # Avanza mientras sea sábado (5) o domingo (6)
        while candidate.weekday() >= 5:
            candidate += timedelta(days=1)

        # ¿Ha saltado de mes? Entonces retrocedemos desde el 27 hacia atrás
        if candidate.month != base_date.month:
            candidate = base_date - timedelta(days=1)
            while candidate.weekday() >= 5:
                candidate -= timedelta(days=1)
        return candidate

    # ─── cálculo fila a fila ───
    def calc_next_payment(row):
        # Sólo nos interesa el tipo “quatrimestral”; el resto se devuelve tal cual
        ptype = row["PAYMENT_TYPE"].strip().lower()
        if ptype != "quatrimestral":
            return None

        # Punto de arranque real (viene de la tabla)
        first = row["FIRST_PAYMENT_DATE"]

        # Partimos del 28 del mes/quartil correcto más cercano ≥ first
        candidate = first.replace(day=TARGET_DAY)

        # Aseguramos que candidate está en un mes 2,5,8,11
        if candidate.month not in QUARTER_MONTHS:
            # Encuentra el próximo mes de la lista
            # Ej.: si first=2025-04-10  → mayo-2025
            future_months = [m for m in QUARTER_MONTHS if m > candidate.month]
            next_month = future_months[0] if future_months else QUARTER_MONTHS[0]
            year_inc   = 0 if future_months else 1
            candidate  = candidate.replace(
                year=candidate.year + year_inc,
                month=next_month,
                day=TARGET_DAY
            )

        # Avanza por ciclos de 3 meses hasta superar hoy
        while candidate <= today_date:
            next_idx  = (QUARTER_MONTHS.index(candidate.month) + 1) % 4
            next_mon  = QUARTER_MONTHS[next_idx]
            year_step = 1 if next_idx == 0 else 0
            candidate = candidate.replace(
                year=candidate.year + year_step,
                month=next_mon,
                day=TARGET_DAY
            )

        # Ajuste a Día Hábil
        candidate = adjust_to_business_day(candidate)
        return candidate.strftime("%d/%m/%Y")

    # Añadimos la columna con la fecha calculada
    df["Next Payment Date"] = df.apply(calc_next_payment, axis=1)

    # Añadimos Cut-Off Date (hoy)
    df["Cut-Off Date"] = today_str

    # Respuesta JSON
    return JSONResponse(content=df.to_dict(orient="records"))
