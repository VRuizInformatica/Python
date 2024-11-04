# Importar la biblioteca pandas, que proporciona estructuras de datos y herramientas de análisis
import pandas as pd
# Importar la biblioteca matplotlib.pyplot, que se utiliza para crear visualizaciones en 2D
import matplotlib.pyplot as plt

# Cargar un conjunto de datos desde un archivo CSV llamado 'data.csv' en un DataFrame
df = pd.read_csv('data.csv')

# Generar un histograma de la columna "Duration" del DataFrame, que muestra la distribución de los datos
df["Duration"].plot(kind='hist')

# Renderizar y mostrar el gráfico en una ventana emergente
plt.show()

# Resumen: Este programa carga un conjunto de datos desde un archivo CSV y genera un histograma de la columna "Duration",
# utilizando pandas para la manipulación de datos y matplotlib para la visualización.