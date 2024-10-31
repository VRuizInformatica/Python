"""Realizar un algoritmo que maneje una lista de enteros a través
de un menú con seis opciones:
1.- Añadir un elemento a la lista
2.- Eliminar un elemento de la lista
3.- Listar el contenido
4.- Contar las apariciones de un número en la lista
5.- Calcular la media y el máximo de los elementos de la lista
0.- Terminar"""

import random  # Importa el módulo random para generar números aleatorios

class Algoritmo:
    """Clase que implementa un algoritmo para manejar una lista de enteros."""

    def __init__(self):
        """Inicializa la clase creando una lista vacía y generando una lista de números aleatorios."""
        self.lista = []  # Inicializa la lista vacía
        self.generarLista()  # Llama al método para generar la lista

    def salir(self):
        """Muestra un mensaje de despedida y termina la ejecución del programa."""
        print("Hasta la proxima")
        exit()  # Termina el programa

    def generarLista(self):
        """Genera una lista de 100 números enteros aleatorios entre 1 y 100."""
        self.lista = [random.randint(1, 100) for _ in range(100)]  # Crea la lista con números aleatorios
        return self.lista  # Devuelve la lista generada
    
    def añadirElementos(self, numAñadir):
        """Añade un número a la lista."""
        self.lista.append(numAñadir)  # Agrega el número al final de la lista

    def eliminarElementos(self, numEliminar):
        """Elimina un número de la lista, si existe."""
        self.lista.remove(numEliminar)  # Elimina la primera aparición del número en la lista

    def listarContenido(self):
        """Devuelve el contenido actual de la lista."""
        return self.lista  # Retorna la lista

    def contadorNums(self, numContador):
        """Cuenta las apariciones de un número en la lista."""
        numRepeticion = 0  # Inicializa el contador de repeticiones
        for i in range(len(self.lista)):  # Itera sobre la lista
            if self.lista[i] == numContador:  # Si el número coincide
                numRepeticion += 1  # Incrementa el contador
        return numRepeticion  # Devuelve el número de repeticiones
    
    def mediaMax(self):
        """Calcula la media y el máximo de los elementos de la lista."""
        numMax = 0  # Inicializa el máximo
        numMedia = 0  # Inicializa la suma para la media
        for i in range(len(self.lista)):  # Itera sobre la lista
            numMedia += self.lista[i]  # Suma los elementos para calcular la media
            if self.lista[i] > numMax:  # Si el elemento actual es mayor que el máximo
                numMax = self.lista[i]  # Actualiza el máximo
        numMedia /= len(self.lista)  # Calcula la media
        return numMax, numMedia  # Devuelve el máximo y la media

    def menu(self):
        """Muestra un menú para interactuar con el usuario y ejecutar las opciones."""
        while True:  # Bucle infinito para mostrar el menú
            respuesta = int(input("0.- Terminar\n1.- Añadir un elemento a la lista\n2.- Eliminar un elemento de la lista\n3.- Listar el contenido\n4.- Contar las apariciones de un número en la lista\n5.- Calcular la media y el máximo de los elementos de la lista\n"))
            if respuesta == 0:  # Opción para salir
                self.salir()
            elif respuesta == 1:  # Opción para añadir un elemento
                self.añadirElementos(int(input("Introduce un numero a añadir\n")))
            elif respuesta == 2:  # Opción para eliminar un elemento
                self.eliminarElementos(int(input("Introduce un numero a eliminar\n")))
            elif respuesta == 3:  # Opción para listar el contenido
                print(self.listarContenido())
            elif respuesta == 4:  # Opción para contar apariciones
                print(self.contadorNums(int(input("Introduce un numero a contar\n"))))
            elif respuesta == 5:  # Opción para calcular media y máximo
                print(self.mediaMax())
            else:  # Opción no válida
                print("Opcion incorrecta")

algoritmo = Algoritmo()  # Crea una instancia de la clase Algoritmo
algoritmo.menu()  # Llama al método menu para iniciar la interacción