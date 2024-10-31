# Programa que suma los numeros de una tabla

def suma(tablaDef):
    # Inicializa la variable resultado en 0 para almacenar la suma
    resultado = 0
    # Itera sobre cada número en la tabla proporcionada
    for num in tablaDef:
        # Suma cada número al resultado acumulado
        resultado += num
    # Imprime el resultado final de la suma
    print(f"Este es el resultado de la suma de los numeros de la tabla: {resultado}")

# Solicita al usuario que ingrese una tabla en formato de lista
tabla = input("Porfavor pasame un tabla en el siguiente formato [1,2,3,4,5]\n")
# Elimina los corchetes de la entrada del usuario
tabla = tabla.replace("[", "")
tabla = tabla.replace("]", "")
# Convierte la cadena de números en una lista de enteros
tablaDef = [int(numero) for numero in tabla.split(",")]
# Llama a la función suma y almacena el resultado
resultado = suma(tablaDef)