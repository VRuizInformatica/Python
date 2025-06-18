import pandas as pd
import oracledb

# ========== CONFIGURACIÓN - MODIFICA AQUÍ ==========

# Credenciales de la base de datos
USERNAME = 'your_username'
PASSWORD = 'your_password'
HOST = 'localhost'
PORT = '1521'
SERVICE_NAME = 'your_service_name'

# Archivos y tabla
EXCEL_FILE = 'your_file.xlsx'
TABLE_NAME = 'your_table'

# Columnas a insertar del Excel
COLUMNS = ['Column1', 'Column2', 'Column3']

# Exclusión (opcional - deja en None si no quieres excluir)
EXCLUDE_COLUMN = 'Status'  # Columna a verificar
EXCLUDE_VALUES = ['CANCELED', 'DELETED']  # Valores a excluir

# ========== CÓDIGO PRINCIPAL ==========

def main():
    try:
        # Leer Excel
        print("Leyendo Excel...")
        df = pd.read_excel(EXCEL_FILE)
        df = df[COLUMNS]  # Solo las columnas que queremos
        print(f"Total filas en Excel: {len(df)}")
        
        # Excluir filas si es necesario
        if EXCLUDE_COLUMN and EXCLUDE_VALUES:
            df = df[~df[EXCLUDE_COLUMN].isin(EXCLUDE_VALUES)]
            print(f"Filas después de filtrar: {len(df)}")
        
        # Conectar a Oracle
        print("Conectando a Oracle...")
        dsn = f"{HOST}:{PORT}/{SERVICE_NAME}"
        connection = oracledb.connect(user=USERNAME, password=PASSWORD, dsn=dsn)
        cursor = connection.cursor()
        
        # Preparar SQL
        placeholders = ', '.join([f':{i+1}' for i in range(len(COLUMNS))])
        column_names = ', '.join(COLUMNS)
        sql = f"INSERT INTO {TABLE_NAME} ({column_names}) VALUES ({placeholders})"
        
        # Insertar datos
        print("Insertando datos...")
        inserted = 0
        for index, row in df.iterrows():
            try:
                # Convertir NaN a None
                values = [None if pd.isna(val) else val for val in row.values]
                cursor.execute(sql, values)
                inserted += 1
            except Exception as e:
                print(f"Error en fila {index + 1}: {e}")
        
        # Guardar y cerrar
        connection.commit()
        cursor.close()
        connection.close()
        
        print(f"¡Completado! Insertadas {inserted} filas")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
