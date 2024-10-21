# Programa que dice la palabra mas larga y la mas corta de una tabla

def masYmenos(tabla):
    masLargo = tabla[0]
    masCorto = tabla[0]

    for palabra in tabla:
        if len(palabra) > len(masLargo):
            masLargo = palabra
        if len(palabra) < len(masCorto):
            masCorto = palabra

    print(f"Esta es la palabra mas larga: {masLargo} con {len(masLargo)}")
    print(f"Esta es la palabra mas corta: {masCorto} con {len(masCorto)}")

tabla = input("Pasame una tabla de nombres: " ).split(",")

masYmenos(tabla)