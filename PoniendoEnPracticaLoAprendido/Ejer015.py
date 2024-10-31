# Crear y escribir en un archivo de texto

# Abre el archivo 'archivo.txt' en modo escritura ('w'), lo que crea el archivo si no existe
with open('archivo.txt', 'w') as file:
    # Escribe una línea de texto en el archivo
    file.write('Hola que haces\n')


# Abre el archivo 'archivo.txt' en modo lectura y escritura ('r+')
with open('archivo.txt', 'r+') as file:
    # Lee todo el contenido del archivo
    contenido = file.read()
    # Inicializa una cadena vacía para almacenar el nuevo contenido sin espacios
    contenidoNuevo = ""
    # Itera sobre cada carácter del contenido leído
    for i in range(len(contenido)):
        # Si el carácter no es un espacio, lo agrega a la nueva cadena
        if contenido[i] != " ":
            contenidoNuevo += contenido[i]
    # Regresa al inicio del archivo para sobrescribirlo
    file.seek(0)
    # Escribe el nuevo contenido sin espacios en el archivo
    file.write(contenidoNuevo)
    # Trunca el archivo para eliminar cualquier contenido restante después del nuevo contenido
    file.truncate()