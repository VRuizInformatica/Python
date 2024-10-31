# Crear una clase llamada Matriz que contenga los siguientes atributos: filas, columnas y una matriz de números enteros. La clase debe tener los siguientes métodos:

class Matriz:
    # Inicialización de los atributos de la clase
    rows = 0
    columns = 0
    def __init__(self, rows, columns, matrix):
        # Constructor que recibe el número de filas, columnas y la matriz
        self.rows = rows
        self.columns = columns
        self.matrix = matrix

    def __str__(self):
        # Método para representar la matriz como una cadena de texto
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

    def getNumberRows(self):
        # Método para obtener el número de filas de la matriz
        return self.rows
    
    def getNumberColumns(self):
        # Método para obtener el número de columnas de la matriz
        return self.columns
    
    def setElement(self, x, j, element):
        # Método para establecer un elemento en la matriz en la posición (x, j)
        if x < self.rows and j < self.columns:
            self.matrix[x][j] = element
        else:
            print("Índice fuera de rango")  # Mensaje de error si el índice está fuera de rango

    def addMatriz(self, otherMatrix):
        # Método para sumar otra matriz a la matriz actual
        if self.rows != len(otherMatrix) or self.columns != len(otherMatrix[0]):
            print("No se puede realizar la operación")  # Mensaje de error si las dimensiones no coinciden
        else:
            for i in range(self.rows):
                for j in range(self.columns):
                    self.matrix[i][j] += otherMatrix[i][j]  # Suma elemento por elemento

    def multMatriz(self, otherMatrix):
        # Método para multiplicar la matriz actual por otra matriz
        if self.rows != len(otherMatrix) or self.columns != len(otherMatrix[0]):
            print("No se puede realizar la operación")  # Mensaje de error si las dimensiones no coinciden
        else:
            for i in range(self.rows):
                for j in range(self.columns):
                    self.matrix[i][j] *= otherMatrix[i][j]  # Multiplicación elemento por elemento

# Creación de un objeto de la clase Matriz con una matriz de 3x3
matrizObj = Matriz(3, 3, [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Impresión de la matriz y el número de filas
print(matrizObj)
print(matrizObj.getNumberRows())