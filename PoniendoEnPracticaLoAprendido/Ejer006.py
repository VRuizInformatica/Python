# Programa que dice la primera y la ultima letra de una palabra

respuesta = input("Soy mago, te voy a decir cual es la primera letra y la ultima de la palabra que me pases\n")
respuesta = respuesta.replace(" ", "")
if len(respuesta) > 1:
    primero = respuesta[0]
    ultimo = respuesta[-1]
    print(f"El primer carácter es: {primero}")
    print(f"El último carácter es: {ultimo}")
else:
    print("La palabra debe tener más de un carácter.")


