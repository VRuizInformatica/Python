"""Realizar un algoritmo que maneje una lista de enteros a través
de un menú con seis opciones:
1.- Añadir un elemento a la lista
2.- Eliminar un elemento de la lista
3.- Listar el contenido
4.- Contar las apariciones de un número en la lista
5.- Calcular la media y el máximo de los elementos de la lista
0.- Terminar"""

import random

class Algoritmo:

    def __init__(self):
        self.lista = []
        self.generarLista()

    def salir(self):
        print("Hasta la proxima")
        exit()

    def generarLista(self):
        self.lista = [random.randint(1, 100) for _ in range(100)]
        return self.lista
    
    def añadirElementos(self, numAñadir):
        self.lista.append(numAñadir)

    def eliminarElementos(self, numEliminar):
        self.lista.remove(numEliminar)

    def listarContenido(self):
        return self.lista

    def contadorNums(self, numContador):
        numRepeticion = 0
        for i in range(len(self.lista)):
            if self.lista[i] == numContador:
                numRepeticion += 1
        return numRepeticion
    
    def mediaMax(self):
        numMax = 0
        numMedia = 0
        for i in range(len(self.lista)):
            numMedia += self.lista[i]
            if self.lista[i] > numMax:
                numMax = self.lista[i]
        numMedia /= len(self.lista)
        return numMax, numMedia

    def menu(self):
        while True:
            respuesta = int(input("0.- Terminar\n1.- Añadir un elemento a la lista\n2.- Eliminar un elemento de la lista\n3.- Listar el contenido\n4.- Contar las apariciones de un número en la lista\n5.- Calcular la media y el máximo de los elementos de la lista\n"))
            if respuesta == 0:
                self.salir()
            elif respuesta == 1:
                self.añadirElementos(int(input("Introduce un numero a añadir\n")))
            elif respuesta == 2:
                self.eliminarElementos(int(input("Introduce un numero a eliminar\n")))
            elif respuesta == 3:
                print(self.listarContenido())
            elif respuesta == 4:
                print(self.contadorNums(int(input("Introduce un numero a contar\n"))))
            elif respuesta == 5:
                print(self.mediaMax())
            else:
                print("Opcion incorrecta")

algoritmo = Algoritmo()
algoritmo.menu()