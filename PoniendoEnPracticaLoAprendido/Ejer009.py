tabla = input("Pásame una tabla (separada por comas) y comprobaré si el elemento se encuentra en ella y en qué posición: \n").split(",")

cadena = input("Pásame lo que quieras que encuentre en la tabla: \n")

encontrado = False

for posicion, num in enumerate(tabla):
    if cadena == num:
        print(f"{cadena} se encuentra en la posición: {posicion + 1}")
        encontrado = True
        break

if not encontrado:
    print(f"No se encuentra {cadena} en la tabla que me has pasado")
