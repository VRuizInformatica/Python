# Programa que dice la palabra mas larga y la mas corta de una tabla

def masYmenos(tabla):
    # Inicializa las variables para la palabra mas larga y mas corta con el primer elemento de la tabla
    masLargo = tabla[0]
    masCorto = tabla[0]

    # Itera sobre cada palabra en la tabla
    for palabra in tabla:
        # Actualiza masLargo si la longitud de la palabra actual es mayor
        if len(palabra) > len(masLargo):
            masLargo = palabra
        # Actualiza masCorto si la longitud de la palabra actual es menor
        if len(palabra) < len(masCorto):
            masCorto = palabra

    # Imprime la palabra mas larga y su longitud
    print(f"Esta es la palabra mas larga: {masLargo} con {len(masLargo)}")
    # Imprime la palabra mas corta y su longitud
    print(f"Esta es la palabra mas corta: {masCorto} con {len(masCorto)}")

tabla = input("Pasame una tabla de nombres: " )
tabla = tabla.replace("[", "")
tabla = tabla.replace("]", "")
tablaDef = tabla.split(",")
masYmenos(tablaDef)