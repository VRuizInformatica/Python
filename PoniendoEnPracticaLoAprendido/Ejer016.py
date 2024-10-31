# Description: Crear una lista de 100 elementos con valores aleatorios entre 1 y 100, ordenarla y eliminar los elementos repetidos.

import random  # Importa el módulo random para generar números aleatorios.

class Ejer016:  # Define la clase Ejer016.

    def lista():  # Método para generar una lista de 100 números aleatorios.
        lista = [random.randint(1, 100) for _ in range(100)]  # Crea una lista con 100 números aleatorios entre 1 y 100.
        print("Lista Desordenada y con repeticiones\n")  # Imprime un mensaje indicando que la lista está desordenada.
        return lista  # Devuelve la lista generada.

    def listaOrdenada(lista):  # Método para ordenar la lista y eliminar duplicados.
        lista = sorted(set(lista))  # Convierte la lista en un conjunto para eliminar duplicados y luego la ordena.
        print("Lista Ordenada y sin repeticiones\n")  # Imprime un mensaje indicando que la lista está ordenada.
        return lista  # Devuelve la lista ordenada y sin duplicados.

    print(lista())  # Llama al método lista() y imprime la lista desordenada.
    print(listaOrdenada(lista()))  # Llama al método listaOrdenada() con la lista desordenada y la imprime.