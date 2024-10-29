# Crear una clase llamada Matriz que contenga los siguientes atributos: filas, columnas y una matriz de números enteros. La clase debe tener los siguientes métodos:

class Matriz:
    rows = 0
    columns = 0
    def __init__(self, rows, columns, matrix):
        self.rows = rows
        self.columns = columns
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

    def getNumberRows(self):
        return self.rows
    
    def getNumberColumns(self):
        return self.columns
    
    def setElement(self, x, j, element):
        if x < self.rows and j < self.columns:
            self.matrix[x][j] = element
        else:
            print("Índice fuera de rango")

    def addMatriz(self, otherMatrix):
        if self.rows != len(otherMatrix) or self.columns != len(otherMatrix[0]):
            print("No se puede realizar la operación")
        else:
            for i in range(self.rows):
                for j in range(self.columns):
                    self.matrix[i][j] += otherMatrix[i][j]

    def multMatriz(self, otherMatrix):
        if self.rows != len(otherMatrix) or self.columns != len(otherMatrix[0]):
            print("No se puede realizar la operación")
        else:
            for i in range(self.rows):
                for j in range(self.columns):
                    self.matrix[i][j] *= otherMatrix[i][j]

matrizObj = Matriz(3, 3, [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(matrizObj)
print(matrizObj.getNumberRows())