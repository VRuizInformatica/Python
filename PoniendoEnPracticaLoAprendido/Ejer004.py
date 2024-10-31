# Programa que cuenta la longitud de una cadena de texto ingresada por el usuario

longitud = 0  # Inicializa la variable longitud en 0

# Solicita al usuario que ingrese una frase y almacena la respuesta
respuesta = input("Soy un contador de cadenas de texto pasame una frase y contare sus caracteres sin contar los espacios\n")

# Calcula la longitud de la cadena sin contar los espacios
longitud = len(respuesta.replace(" ", ""))

# Imprime la longitud de la cadena ingresada
print(f"La longitud de '{respuesta}' es de: {longitud}")