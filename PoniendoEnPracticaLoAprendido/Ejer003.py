import random

numeroGanador = (random.randint(0,20))
intentos = 5

print("Buenisimos dias, hoy vas a jugar a !ADIVINA MI NUMERITO¡")
respuestaSINO = input("Te apetece jugar? (si/no)")

if respuestaSINO == "si":

    for i in range (0,5):
        print(f"Tienes {intentos} intentos, a la {intentos} va la vencida, ya verás")
        respuesta = int(input("Introduzca su siguiente numero"))
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