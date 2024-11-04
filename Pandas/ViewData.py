# Importar la biblioteca pandas para el manejo de datos
import pandas as pd

# Leer un archivo CSV llamado 'data.csv' y almacenarlo en un DataFrame
df = pd.read_csv('data.csv')

# Mostrar las primeras 10 filas del DataFrame
print(df.head(10))
# Mostrar las últimas 5 filas del DataFrame
print(df.tail()) 