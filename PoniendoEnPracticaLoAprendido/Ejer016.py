# Description: Crear una lista de 100 elementos con valores aleatorios entre 1 y 100, ordenarla y eliminar los elementos repetidos.

import random

class Ejer016:

    def lista():
        lista = [random.randint(1, 100) for _ in range(100)]
        print("Lista Desordenada y con repeticiones\n")
        return lista

    def listaOrdenada(lista):
        lista = sorted(set(lista))
        print("Lista Ordenada y sin repeticiones\n")
        return lista

    print(lista())
    print(listaOrdenada(lista()))