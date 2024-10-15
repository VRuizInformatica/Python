def suma(tablaDef):
    resultado = 0
    for num in (tablaDef):
        resultado = resultado + num
    print(f"Este es el resultado de la suma de los numeros de la tabla: {resultado}")

tabla = input("Porfavor pasame un tabla en el siguiente formato (1,2,3,4,5)")

tablaDef = [int(numero) for numero in tabla.split(",")]

suma(tablaDef)