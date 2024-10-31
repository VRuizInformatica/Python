# Programa que recibe dos números y una operación a realizar, devuelve el resultado de la operación

def calculadora(respuesta, uno, dos):
    # Inicializa el resultado en 0
    resultado = 0
    # Verifica la operación solicitada y realiza el cálculo correspondiente
    if respuesta == "sumar":
        resultado = uno + dos  # Suma
    elif respuesta == "restar":
        resultado = uno - dos  # Resta
    elif respuesta == "multiplicar":
        resultado = uno * dos  # Multiplicación
    elif respuesta == "dividir":
        resultado = uno / dos  # División
    else:
        resultado = uno % dos  # Resto
    # Imprime el resultado de la operación
    print(f"El resultado de la operacion es {resultado}")

# Lista de operaciones válidas
listaAcceso = ["sumar", "restar", "multiplicar", "dividir", "resto"]

# Solicita al usuario la operación que desea realizar
respuesta = input("Buenos dias soy una calculadora, Que operacion desea hacer hoy? (sumar, restar, multiplicar, dividir, resto)\n").lower()

# Verifica si la respuesta está en la lista de operaciones válidas
if respuesta in listaAcceso:
    # Solicita el primer número al usuario
    uno = int(input(f"Perfecto que numero deseas {respuesta}?\n"))

    # Solicita el segundo número según la operación elegida
    if respuesta == "sumar":
        dos = int(input(f"Que numero desea sumarle a {uno}?\n"))
    elif respuesta == "restar":
        dos = int(input(f"Que numero desea restarle a {uno}?\n"))
    elif respuesta == "multiplicar":
        dos = int(input(f"Por que numero desea multiplicar {uno}?\n"))
    elif respuesta == "dividir":
        dos = int(input(f"Por que numero desea dividir {uno}?\n"))
    else:
        dos = int(input(f"Por que numero desea dividir {uno} para hayar su resto?\n"))

    # Llama a la función calculadora con los números y la operación seleccionada
    calculadora(respuesta, uno, dos)

else:
    # Mensaje de error si la operación no es válida
    print("Lo lamento pero no comprendo su mensaje recuerde introducir solo una de estas opciones (sumar, restar, multiplicar, dividir, resto)")