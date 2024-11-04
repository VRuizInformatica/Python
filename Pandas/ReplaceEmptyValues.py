# Importar la biblioteca pandas para el manejo de datos
import pandas as pd
# Importar la biblioteca matplotlib.pyplot para la visualización de datos
import matplotlib.pyplot as plt

# Leer un archivo CSV llamado 'data.csv' y almacenarlo en un DataFrame
df = pd.read_csv('data.csv')

# Crear un gráfico de área utilizando los datos del DataFrame
df.plot(kind='area')

# Mostrar el gráfico generado en una ventana emergente
plt.show()

# Resumen: Este programa carga un conjunto de datos desde un archivo CSV y genera un gráfico de área
# utilizando pandas para la manipulación de datos y matplotlib para la visualización.