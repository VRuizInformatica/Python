import random  # Importa el módulo random para generar números aleatorios

# Juego de adivinar un número aleatorio entre 0 y 20 con 5 intentos
# Nivel 1

numeroGanador = (random.randint(0,20))  # Genera un número aleatorio entre 0 y 20
intentos = 5  # Establece el número de intentos permitidos

print("Buenisimos dias, hoy vas a jugar a !ADIVINA MI NUMERITO¡, ")
respuestaSINO = input("Te apetece jugar? (si/no)\n").lower()  # Pregunta al usuario si quiere jugar

if respuestaSINO == "si":  # Si el usuario acepta jugar

    for i in range (0,5):  # Bucle para los 5 intentos
        print(f"Tienes {intentos} intentos, a la {i+1}""º"" va la vencida, ya verás")
        respuesta = int(input("Introduzca su siguiente numero\n"))  # Solicita un número al usuario
        intentos = intentos -1  # Reduce el número de intentos restantes
        if respuesta < numeroGanador:  # Compara la respuesta con el número ganador
            print("El numero que buscas es mayor")
        elif respuesta > numeroGanador:
            print("El numero que buscas es menor")
        elif respuesta == numeroGanador:  # Si el usuario adivina el número
            print("Vamoooos acertaste OLEEEEEEE")
            break  # Sale del bucle si se adivina el número
        else:
            print("Porfavor introduzca numeros enteros, vuelva a intentarlo")  # Mensaje de error para entradas no válidas

    # Nivel 2
    numeroGanador2 = (random.randint(0,30))  # Genera un número aleatorio entre 0 y 30
    intentos2 = 5  # Establece el número de intentos para el nivel 2

    print("Eres una BESTIA! vamos a complicarlo un poquito mas, ahora el numero a adivinar esta entre 0 y 30")
    respuestaSINO2 = input("Te atreves? (si/no)\n").lower()  # Pregunta al usuario si quiere continuar al nivel 2

    if respuestaSINO2 == "si":  # Si el usuario acepta jugar el nivel 2

        for i in range (0,5):  # Bucle para los 5 intentos en el nivel 2
            print(f"Tienes {intentos2} intentos")
            respuesta2 = int(input("Introduzca su siguiente numero\n"))  # Solicita un número al usuario
            intentos2 = intentos2 -1  # Reduce el número de intentos restantes
            if respuesta2 < numeroGanador2:
                print("El numero que buscas es mayor")
            elif respuesta2 > numeroGanador2:
                print("El numero que buscas es menor")
            elif respuesta2 == numeroGanador2:  # Si el usuario adivina el número
                print("Vamoooos acertaste OLEEEEEEE")
                break  # Sale del bucle si se adivina el número
            else:
                print("Porfavor introduzca numeros enteros, vuelva a intentarlo")  # Mensaje de error para entradas no válidas

        # Nivel 3
        numeroGanador3 = (random.randint(0,50))  # Genera un número aleatorio entre 0 y 50 para el nivel 3
        intentos3 = 5  # Establece el número de intentos para el nivel 3

        print("Ya veo que eres de los expertos, has llegado al nivel mas dificil veamos si lo consigues, el numero a adivinar esta entre 0-50")
        respuestaSINO3 = input("Te atreves? (si/no)\n").lower()  # Pregunta al usuario si quiere continuar al nivel 3

        if respuestaSINO3 == "si":  # Si el usuario acepta jugar el nivel 3
            for i in range (0,5):  # Bucle para los 5 intentos en el nivel 3
                print(f"Tienes {intentos3} intentos")
                respuesta3 = int(input("Introduzca su siguiente numero\n"))  # Solicita un número al usuario
                intentos3 = intentos3 -1  # Reduce el número de intentos restantes
                if respuesta3 < numeroGanador3:
                    print("El numero que buscas es mayor")
                elif respuesta3 > numeroGanador3:
                    print("El numero que buscas es menor")
                elif respuesta3 == numeroGanador3:  # Si el usuario adivina el número
                    print("Dios mio que crack, eres un dios te pasaste !ADIVINA MI NUMERITO¡ ")
                    print("Gracias por jugar =)")
                    break  # Sale del bucle si se adivina el número
                else:
                    print("Porfavor introduzca numeros enteros, vuelva a intentarlo")  # Mensaje de error para entradas no válidas
        else:
            print("La cobardia es tu peor enemigo, adios.")  # Mensaje si el usuario no quiere jugar el nivel 3
    else:
        print("La cobardia es tu peor enemigo, adios.")  # Mensaje si el usuario no quiere jugar el nivel 2
else:
    print("A vale bueno pues nada que te vaya bien.")  # Mensaje si el usuario no quiere jugar
