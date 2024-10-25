import random

# Juego de adivinar un numero aleatorio entre 0 y 20 con 5 intentos
# Nivel 1

numeroGanador = (random.randint(0,20))
intentos = 5

print("Buenisimos dias, hoy vas a jugar a !ADIVINA MI NUMERITO¡, el numero a adivinar esta entre 0 y 20")
respuestaSINO = input("Te apetece jugar? (si/no)\n").lower()

if respuestaSINO == "si":

    for i in range (0,5):
        print(f"Tienes {intentos} intentos, a la {i+1}""º"" va la vencida, ya verás")
        respuesta = int(input("Introduzca su siguiente numero\n"))
        intentos = intentos -1
        if respuesta < numeroGanador:
            print("El numero que buscas es mayor")
        elif respuesta > numeroGanador:
            print("El numero que buscas es menor")
        elif respuesta == numeroGanador:
            print("Vamoooos acertaste OLEEEEEEE")
            break
        else:
            print("Porfavor introduzca numeros enteros, vuelva a intentarlo")



    # Nivel 2
    numeroGanador2 = (random.randint(0,30))
    intentos2 = 5

    print("Eres una BESTIA! vamos a complicarlo un poquito mas, ahora el numero a adivinar esta entre 0 y 30")
    respuestaSINO2 = input("Te atreves? (si/no)\n").lower()

    if respuestaSINO2 == "si":

        for i in range (0,5):
            print(f"Tienes {intentos2} intentos")
            respuesta2 = int(input("Introduzca su siguiente numero\n"))
            intentos2 = intentos2 -1
            if respuesta2 < numeroGanador2:
                print("El numero que buscas es mayor")
            elif respuesta2 > numeroGanador2:
                print("El numero que buscas es menor")
            elif respuesta2 == numeroGanador2:
                print("Vamoooos acertaste OLEEEEEEE")
                break
            else:
                print("Porfavor introduzca numeros enteros, vuelva a intentarlo")

        # Nivel 3
        numeroGanador3 = (random.randint(0,30))
        intentos3 = 5

        print("Ya veo que eres de los expertos, has llegado al nivel mas dificil veamos si lo consigues, el numero a adivinar esta entre 0-50")
        respuestaSINO3 = input("Te atreves? (si/no)\n").lower()

        if respuestaSINO3 == "si":
            for i in range (0,5):
                print(f"Tienes {intentos3} intentos")
                respuesta3 = int(input("Introduzca su siguiente numero\n"))
                intentos3 = intentos3 -1
                if respuesta3 < numeroGanador3:
                    print("El numero que buscas es mayor")
                elif respuesta3 > numeroGanador3:
                    print("El numero que buscas es menor")
                elif respuesta3 == numeroGanador3:
                    print("Dios mio que crack, eres un dios te pasaste !ADIVINA MI NUMERITO¡ ")
                    print("Gracias por jugar =)")
                    break
                else:
                    print("Porfavor introduzca numeros enteros, vuelva a intentarlo")
        else:
            print("La cobardia es tu peor enemigo, adios.")
    else:
        print("La cobardia es tu peor enemigo, adios.")
else:
    print("A vale bueno pues nada que te vaya bien.")
