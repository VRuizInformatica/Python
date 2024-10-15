contadorCeros = 0
contadorMayores = 0
contadorMenores = 0

print("Hola buenos dias, me podrias pasar 10 numeros enteros? (si/no)")
respuesta = input()

if respuesta == "si":
    print("Perfecto pues pongamonos a ello introduce los 10 numeros a continuacion")
    
    for i in range(10):
        numero = int(input(f"Introduce el numero {i+1}: "))
        
        if numero == 0:
            contadorCeros = contadorCeros + 1
        elif numero > 0:
            contadorMayores = contadorMayores + 1
        else:
            contadorMenores = contadorMenores + 1

    print(f"Total de ceros introducidos: {contadorCeros}")
    print(f"Total de numeros mayores que 0: {contadorMayores}")
    print(f"Total de numeros menores que 0: {contadorMenores}")

else:
    print("Ah bueno, pues nada, adios...")
