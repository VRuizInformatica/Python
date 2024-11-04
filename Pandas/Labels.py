# Importar la biblioteca pandas para el manejo de datos
import pandas as pd
# Importar la biblioteca matplotlib.pyplot para la visualización de datos
import matplotlib.pyplot as plt

# Leer un archivo CSV llamado 'data.csv' y almacenarlo en un DataFrame
df = pd.read_csv('data.csv')

# Crear un gráfico de barras utilizando la columna 'Category' como eje x y 'Values' como eje y
df.plot(kind='bar', x='Category', y='Values')

# Mostrar el gráfico generado en una ventana emergente
plt.show()

# Resumen: Este programa carga un conjunto de datos desde un archivo CSV y genera un gráfico de barras
# utilizando la columna 'Category' para el eje x y 'Values' para el eje y, utilizando pandas para la
# manipulación de datos y matplotlib para la visualización.