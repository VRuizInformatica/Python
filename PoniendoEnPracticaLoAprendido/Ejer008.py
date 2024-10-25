# Programa que suma los numeros de una tabla

def suma(tablaDef):
    resultado = 0
    for num in tablaDef:
        resultado += num
    print(f"Este es el resultado de la suma de los numeros de la tabla: {resultado}")

tabla = input("Porfavor pasame un tabla en el siguiente formato [1,2,3,4,5]\n")
tabla = tabla.replace("[", "")
tabla = tabla.replace("]", "")
tablaDef = [int(numero) for numero in tabla.split(",")]
resultado = suma(tablaDef)