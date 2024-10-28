def calculadora(respuesta, uno, dos):
    resultado=0
    if respuesta == "sumar":
        resultado = uno + dos
    elif respuesta == "restar":
        resultado = uno - dos
    elif respuesta == "multiplicar":
        resultado = uno * dos
    elif respuesta == "dividir":
        resultado = uno / dos
    else:
        resultado = uno % dos
    print(f"El resultado de la operacion es {resultado}")

listaAcceso = ["sumar", "restar", "multiplicar", "dividir", "resto"]

respuesta = input("Buenos dias soy una calculadora, Que operacion desea hacer hoy? (sumar, restar, multiplicar, dividir, resto)\n").lower()

if respuesta in listaAcceso:

    uno = int(input(f"Perfecto que numero deseas {respuesta}?\n"))

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

    calculadora(respuesta, uno , dos)

else:
    print("Lo lamento pero no comprendo su mensaje recuerde introducir solo una de estas opciones (sumar, restar, multiplicar, dividir, resto)")