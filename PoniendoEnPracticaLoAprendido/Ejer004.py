# Programa que cuenta la longitud de una cadena de texto ingresada por el usuario

longitud = 0

respuesta = input("Soy un contador de cadenas de texto pasame una frase y contare sus caracteres sin contar los espacios\n")
longitud = len(respuesta.replace(" ", ""))

print(f"La longitud de '{respuesta}' es de: {longitud}")
