# Programa que evita que el usuario escriba la palabra "aaa"

cadenaDelmiedo = "aaa"

respuesta = input("No me gusta nada 'aaa' asi que ni se te ocurra escribirmelo\n").lower()
if cadenaDelmiedo in respuesta:
    print("NOoooooOoooOoo te dije que no me gusta nadaaaaaaa")
else:
    print("Sabia que eras de fiar =)")
