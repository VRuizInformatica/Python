# Importar la biblioteca pandas para el manejo de datos
import pandas as pd
# Importar la biblioteca matplotlib.pyplot para la visualización de datos
import matplotlib.pyplot as plt

# Leer un archivo CSV llamado 'data.csv' y almacenarlo en un DataFrame
df = pd.read_csv('data.csv')

# Crear un gráfico de dispersión utilizando las columnas 'Duration' y 'Calories' del DataFrame
df.plot(kind='scatter', x='Duration', y='Calories')

# Mostrar el gráfico generado en una ventana emergente
plt.show()

# Resumen: Este programa carga un conjunto de datos desde un archivo CSV y genera un gráfico de dispersión
# que muestra la relación entre las columnas 'Duration' y 'Calories', utilizando pandas para la manipulación
# de datos y matplotlib para la visualización.