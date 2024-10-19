suma = 0
resta = 0
multiplicacion = 0
division = 0

respuesta = input("Que operacion quieres hacer? (Suma, Resta, Multiplicacion, Division): \n").lower()
num1 = int(input("Dame el primer numero: \n"))
num2 = int(input("Dame el segundo numero: \n"))

def opera1(respuesta, num1, num2):
    if respuesta == 'suma':
        suma = num1 + num2
        print(f"El resultado de la operacion es: {suma}")
    elif respuesta == 'resta':
        resta = num1 - num2
        print(f"El resultado de la operacion es: {resta}")
    elif respuesta == 'multiplicacion':
        multiplicacion = num1 * num2
        print(f"El resultado de la operacion es: {multiplicacion}")
    elif respuesta == 'division':
        division = num1 / num2
        print(f"El resultado de la operacion es: {division}")
    else:
        print("Operacion no valida")
    
opera1(respuesta, num1, num2)