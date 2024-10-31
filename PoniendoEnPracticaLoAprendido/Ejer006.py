# Programa que dice la primera y la ultima letra de una palabra

respuesta = input("Soy mago, te voy a decir cual es la primera letra y la ultima de la palabra que me pases\n")  # Solicita al usuario una palabra
respuesta = respuesta.replace(" ", "")  # Elimina los espacios en blanco de la respuesta
if len(respuesta) > 1:  # Verifica si la longitud de la palabra es mayor a 1
    primero = respuesta[0]  # Obtiene la primera letra
    ultimo = respuesta[-1]  # Obtiene la última letra
    print(f"El primer carácter es: {primero}")  # Imprime la primera letra
    print(f"El último carácter es: {ultimo}")  # Imprime la última letra
else:
    print("La palabra debe tener más de un carácter.")  # Mensaje de error si la palabra es demasiado corta