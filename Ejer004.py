respuesta = input("Soy un contador de cadenas de texto pasme una frase y contare sus caracteres \n")

longitud = 0

for i in respuesta:
    longitud = longitud+1

print("Esta es la longitud de '" + respuesta + "': " + str(longitud))
