# Crear y escribir en un archivo de texto

with open('archivo.txt', 'w') as file:
    file.write('Hola que haces\n')


with open('archivo.txt', 'r+') as file:
    contenido = file.read()
    contenidoNuevo = ""
    for i in range(len(contenido)):
        if contenido[i] != " ":
            contenidoNuevo += contenido[i]
    file.seek(0)
    file.write(contenidoNuevo)
    file.truncate()