# Crea un programa que pida al usuario 10 números enteros, los almacene en una lista y luego muestre cuántos de esos números son mayores que 0, cuántos menores que 0 y cuántos iguales a 0.

contadorCeros = 0  # Contador para ceros
contadorMayores = 0  # Contador para números mayores que 0
contadorMenores = 0  # Contador para números menores que 0

respuesta = input("Hola buenos dias, me podrias pasar 10 numeros enteros? (si/no)\n").lower()  # Solicita la respuesta del usuario

def Contador(respuesta, contadorCeros, contadorMayores, contadorMenores):
    if respuesta == "si":  # Verifica si el usuario acepta introducir números
        print("Perfecto pues pongamonos a ello introduce los numeros a continuacion\n")

        for i in range(10):  # Bucle para solicitar 10 números
            try:
                numero = int(input(f"Introduce el numero {i+1}: "))  # Solicita un número entero
                if numero == 0:
                    contadorCeros += 1  # Incrementa el contador de ceros
                elif numero > 0:
                    contadorMayores += 1  # Incrementa el contador de números mayores que 0
                else:
                    contadorMenores += 1  # Incrementa el contador de números menores que 0
            except ValueError:  # Manejo de excepciones para entradas no válidas
                print("Por favor, introduce un número entero válido.")
                return  # Sale de la función si hay un error
        print("Gracias por tu colaboracion, los resultados son los siguientes:")
        print(f"Total de ceros introducidos: {contadorCeros}")  # Muestra el total de ceros
        print(f"Total de numeros mayores que 0: {contadorMayores}")  # Muestra el total de números mayores que 0
        print(f"Total de numeros menores que 0: {contadorMenores}")  # Muestra el total de números menores que 0
    else:
        print("A vale bueno pues nada adios...")  # Mensaje de despedida si el usuario no quiere participar

Contador(respuesta, contadorCeros, contadorMayores, contadorMenores)  # Llama a la función Contador