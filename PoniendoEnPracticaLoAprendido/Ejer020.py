def es_escalonada_filas(matriz):
    """
    Verifica si una matriz es escalonada en filas.
    """
    numero_ceros_anterior = -1
    for fila in matriz:
        numero_ceros = 0
        for elemento in fila:
            if elemento == 0:
                numero_ceros += 1
            else:
                break
        if numero_ceros != numero_ceros_anterior + 1:
            return False
        numero_ceros_anterior = numero_ceros
    return True

def es_escalonada_columnas(matriz):
    """
    Verifica si una matriz es escalonada en columnas.
    """
    numero_ceros_anterior = -1
    num_filas = len(matriz)
    num_columnas = len(matriz[0]) if num_filas > 0 else 0

    for col in range(num_columnas):
        numero_ceros = 0
        for fila in range(num_filas):
            if matriz[fila][col] == 0:
                numero_ceros += 1
            else:
                break
        if numero_ceros != numero_ceros_anterior + 1:
            return False
        numero_ceros_anterior = numero_ceros
    return True

# Ejemplos de uso:

# Matriz escalonada en filas
matriz_filas = [
    [1, 2, 3],
    [0, 4, 5],
    [0, 0, 6]
]

# Matriz escalonada en columnas
matriz_columnas = [
    [1, 0, 0],
    [2, 3, 0],
    [4, 5, 6]
]

# Matriz no escalonada
matriz_no_escalonada = [
    [1, 0, 3],
    [0, 2, 5],
    [0, 0, 6]
]

# Verificaciones
if es_escalonada_filas(matriz_filas):
    print("La matriz es escalonada en filas.")
else:
    print("La matriz NO es escalonada en filas.")

if es_escalonada_columnas(matriz_columnas):
    print("La matriz es escalonada en columnas.")
else:
    print("La matriz NO es escalonada en columnas.")

if es_escalonada_filas(matriz_no_escalonada):
    print("La matriz es escalonada en filas.")
else:
    print("La matriz NO es escalonada en filas.")


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list3 = []
        for l1 in list1:
            for l2 in list2:
                if l1 > l2:
                    list3.append(l1)
                    list3.append(l2)
                elif l2 > l1:
                    list3.append(l2)
                    list3.append(l1)
                else:
                    list3.append(l1,l2)
        return list3