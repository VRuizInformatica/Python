def masYmenos(tabla):
    masLargo = tabla[0]
    masCorto = tabla[0]

    for palabra in tabla:
        if len(palabra) > len(masLargo):
            masLargo = palabra
        if len(palabra) < len(masCorto):
            masCorto = palabra

def suma(tablaDef):
    resultado = 0
    for num in (tablaDef):
        resultado = resultado + num


