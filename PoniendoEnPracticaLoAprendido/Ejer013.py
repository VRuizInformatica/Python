# Programa que simula una matriz

class Matriz:
    # Clase que representa una matriz y tiene metodos para manejarla.

    # Inicializa la matriz con un numero de filas y columnas.
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = [[0 for _ in range(columnas)] for _ in range(filas)]

    # Devuelve el numero de filas de la matriz.
    def numero_filas(self):
        return self.filas

    # Devuelve el numero de columnas de la matriz.
    def numero_columnas(self):
        return self.columnas

    # Cambia el valor de la matriz en [x][j] por el valor de [element].
    def poner_elemento(self, x, j, elemento):
        if self.validar_indices(x, j):
            self.matriz[x][j] = elemento
        else:
            print("Indices fuera de rango")

    # Suma todos los elementos de la matriz actual a los de [matrix].
    def sumar_matriz(self, otra_matriz):
        if self.validar_dimensiones(otra_matriz):
            for i in range(self.filas):
                self.matriz[i] = [a + b for a, b in zip(self.matriz[i], otra_matriz[i])]
        else:
            print("No se puede hacer la suma: dimensiones mal")

    # Multiplica todos los elementos de la matriz actual con los de [matrix].
    def multiplicar_matriz(self, otra_matriz):
        if self.validar_dimensiones(otra_matriz):
            resultado = [[0 for _ in range(self.columnas)] for _ in range(self.filas)]
            for i in range(self.filas):
                for j in range(self.columnas):
                    for k in range(self.columnas):
                        resultado[i][j] += self.matriz[i][k] * otra_matriz[k][j]
            self.matriz = resultado
        else:
            print("No se puede hacer la multiplicacion: dimensiones mal")

    # Valida que los indices esten dentro de los limites de la matriz.
    def validar_indices(self, x, j):
        return 0 <= x < self.filas and 0 <= j < self.columnas

    # Valida que las dimensiones de la matriz sean correctas.
    def validar_dimensiones(self, otra_matriz):
        return len(otra_matriz) == self.filas and len(otra_matriz[0]) == self.columnas

    # Devuelve una representacion en cadena de la matriz.
    def __str__(self):
        return '\n'.join([' '.join(map(str, fila)) for fila in self.matriz])

# Ejemplo de uso
mi_matriz = Matriz(3, 3)  # Crea una matriz de 3x3
mi_matriz.poner_elemento(0, 0, 1)  # Pone el elemento en la posicion (0, 0)
mi_matriz.poner_elemento(1, 1, 2)  # Pone el elemento en la posicion (1, 1)
mi_matriz.poner_elemento(2, 2, 3)  # Pone el elemento en la posicion (2, 2)

# Imprime el numero de filas y columnas
print(f"Numero de filas: {mi_matriz.numero_filas()}")
print(f"Numero de columnas: {mi_matriz.numero_columnas()}")

otra_matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Define otra matriz
mi_matriz.sumar_matriz(otra_matriz)  # Suma la otra matriz a la actual

mi_matriz.multiplicar_matriz(otra_matriz)  # Multiplica la matriz actual por la otra

# Intenta operaciones con matrices de dimensiones incorrectas
matriz_incorrecta = [[1, 2], [3, 4]]  # Definir una matrz con dimensiones incorrectas
mi_matriz.sumar_matriz(matriz_incorrecta)  # Intenta sumar la matriz incorrecta
mi_matriz.multiplicar_matriz(matriz_incorrecta)  # Intenta multiplicar la matriz incorrecta
