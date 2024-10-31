# Programa que busca un elemento en una tabla

# Se solicita al usuario que ingrese una tabla de elementos separados por comas
tabla = input("Pásame una tabla (separada por comas) y comprobaré si el elemento se encuentra en ella y en qué posición: \n").split(",")

# Se solicita al usuario que ingrese el elemento que desea buscar en la tabla
cadena = input("Pásame lo que quieras que encuentre en la tabla: \n")

# Variable que indica si el elemento ha sido encontrado
encontrado = False

# Se itera sobre la tabla utilizando enumerate para obtener tanto la posición como el valor del elemento
for posicion, num in enumerate(tabla):
    # Se compara el elemento ingresado con el elemento actual de la tabla
    if cadena == num:
        # Si se encuentra el elemento, se imprime su posición (sumando 1 para que sea más intuitivo)
        print(f"{cadena} se encuentra en la posición: {posicion + 1}")
        # Se marca como encontrado
        encontrado = True
        # Se sale del bucle ya que no es necesario seguir buscando
        break

# Si el elemento no fue encontrado, se informa al usuario
if not encontrado:
    print(f"No se encuentra {cadena} en la tabla que me has pasado")
