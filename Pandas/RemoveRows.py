# Importar la biblioteca pandas para el manejo de datos
import pandas as pd
# Importar la biblioteca matplotlib.pyplot para la visualización de datos
import matplotlib.pyplot as plt
# Importar la biblioteca seaborn para crear gráficos estadísticos
import seaborn as sns

# Leer un archivo CSV llamado 'data.csv' y almacenarlo en un DataFrame
df = pd.read_csv('data.csv')

# Crear un mapa de calor (heatmap) utilizando el DataFrame
# Se utiliza el método corr() para calcular la matriz de correlación
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')

# Mostrar el gráfico generado en una ventana emergente
plt.show()

# Resumen: Este programa carga un conjunto de datos desde un archivo CSV y genera un mapa de calor
# que muestra la matriz de correlación entre las variables del DataFrame, utilizando pandas para la
# manipulación de datos, seaborn para la visualización y matplotlib para mostrar el gráfico.