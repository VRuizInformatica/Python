# Importar la biblioteca pandas para el manejo de datos
import pandas as pd
# Importar la biblioteca matplotlib.pyplot para la visualización de datos
import matplotlib.pyplot as plt

# Leer un archivo CSV llamado 'data.csv' y almacenarlo en un DataFrame
df = pd.read_csv('data.csv')

# Crear un gráfico de pastel (pie chart) utilizando la columna 'Category' para las etiquetas y 'Values' para los tamaños
df.plot(kind='pie', y='Values', labels=df['Category'], autopct='%1.1f%%')

# Mostrar el gráfico generado en una ventana emergente
plt.show()

# Resumen: Este programa carga un conjunto de datos desde un archivo CSV y genera un gráfico de pastel
# utilizando la columna 'Category' para las etiquetas y 'Values' para los tamaños, utilizando pandas para
# la manipulación de datos y matplotlib para la visualización.