# Programa que evita que el usuario escriba la palabra "aaa"

# Se define la cadena que se quiere evitar
cadenaDelmiedo = "aaa"

# Se solicita al usuario que ingrese una respuesta, convirtiéndola a minúsculas
respuesta = input("No me gusta nada 'aaa' así que ni se te ocurra escribírmelo\n").lower()

# Se verifica si la cadena prohibida está en la respuesta del usuario
if cadenaDelmiedo in respuesta:
    # Si el usuario escribió "aaa", se muestra un mensaje de advertencia
    print("NOoooooOoooOoo te dije que no me gusta nadaaaaaaa")
else:
    # Si el usuario no escribió "aaa", se muestra un mensaje de confianza
    print("Sabía que eras de fiar =)")
