"""Dada una matriz cuadrada A, construye un programa Python que permite determinar si dicha matriz es simétrica. Se
considera a una matriz simétrica si A (i , j) = A (j , i) y esto se
cumple para todos los elementos i , j de la matriz."""

class Ejer017:
    def matrizSimetrica():
        # Definición de una matriz cuadrada de ejemplo
        matrizSimetrica = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
        return matrizSimetrica

    def comprobar(matrizSimetrica):
        # Itera sobre cada elemento de la matriz para verificar la simetría
        for i in range(len(matrizSimetrica)):
            for j in range(len(matrizSimetrica[i])):
                # Compara el elemento (i, j) con el elemento (j, i)
                if matrizSimetrica[i][j] != matrizSimetrica[j][i]:
                    # Si no son iguales, imprime que no es simétrica y termina el programa
                    print(f"{matrizSimetrica}\n No es simetrica")
                    exit
        # Si todos los elementos son simétricos, imprime que es simétrica
        print(f"{matrizSimetrica}\n Es simetrica")

    # Llama a la función comprobar con la matriz definida
    comprobar(matrizSimetrica())