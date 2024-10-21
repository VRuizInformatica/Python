# Crea un programa que pida al usuario 10 números enteros, los almacene en una lista y luego muestre cuántos de esos números son mayores que 0, cuántos menores que 0 y cuántos iguales a 0.

contadorCeros = 0
contadorMayores = 0
contadorMenores = 0

respuesta = input("Hola buenos dias, me podrias pasar 10 numeros enteros? (si/no)\n").lower()

def Contador(respuesta):
    global contadorCeros, contadorMayores, contadorMenores
    if respuesta == "si":
        print("Perfecto pues pongamonos a ello introduce los numeros a continuacion\n")

        for i in range(10):
            try:
                numero = int(input(f"Introduce el numero {i+1}: "))
                if numero == 0:
                    contadorCeros += 1
                elif numero > 0:
                    contadorMayores += 1
                else:
                    contadorMenores += 1
            except ValueError:
                print("Por favor, introduce un número entero válido.")
                return
    else:
        print("A vale bueno pues nada adios...")
    
    if respuesta == "si":
        print("Gracias por tu colaboracion, los resultados son los siguientes:")
        print(f"Total de ceros introducidos: {contadorCeros}")
        print(f"Total de numeros mayores que 0: {contadorMayores}")
        print(f"Total de numeros menores que 0: {contadorMenores}")

Contador(respuesta)