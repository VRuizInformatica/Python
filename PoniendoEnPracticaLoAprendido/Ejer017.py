"""Dada una matriz cuadrada A, construye un programa Python que permita determinar si dicha matriz es simétrica. Se
considera a una matriz simétrica si A (i , j) = A (j , i) y esto se
cumple para todos los elementos i , j de la matriz."""

class Ejer017:
    def matrizSimetrica():
        matrizSimetrica = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
        return matrizSimetrica

    def comprobar(matrizSimetrica):
        for i in range(len(matrizSimetrica)):
            for j in range(len(matrizSimetrica[i])):
                if matrizSimetrica[i][j] != matrizSimetrica[j][i]:
                    print(f"{matrizSimetrica}\n No es simetrica")
                    exit
        print(f"{matrizSimetrica}\n Es simetrica")

    comprobar(matrizSimetrica())