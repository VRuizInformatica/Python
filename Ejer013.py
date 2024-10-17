class Matriz:

    mi_matriz = Matriz(3, 3)

# Cambiar el valor en la posición [1][2] a 99
    mi_matriz.setElement(1, 2, 99)

# Mostrar la matriz
    mi_matriz.mostrar()

    def __init__(self, filas, columnas):
        self.matriz = [[0 for _ in range(columnas)] for _ in range(filas)]

    def getNumberRows(self):
        return self.rows

    def getNumberColumns(self):
        return self.colums

    def setElement(self, x, j, element):


    def addMatrix(self, matrix):

    def multMatrix(self, matrix):