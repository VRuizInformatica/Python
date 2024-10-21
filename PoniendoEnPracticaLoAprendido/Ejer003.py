import random

# Juego de adivinar un numero aleatorio entre 0 y 20 con 5 intentos

numeroGanador = (random.randint(0,20))
intentos = 5

print("Buenisimos dias, hoy vas a jugar a !ADIVINA MI NUMERITO¡")
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
            print("Gracias por jugar =)")
        else:
            print("Porfavor introduzca numeros enteros, vuelva a intentarlo")

else:
    print("A vale bueno pues nada que te vaya bien.")