# Crear un programa que muestre los números pares del 1 al 100

def lista():
    listaDef = []
    for i in range(1, 101):
        if i % 2 == 0:
            listaDef = listaDef + [i]
    return listaDef

def lectura():
    return(lista())

def salir():
    print("Hasta luego")
    exit()

def menu():
    opcion = input("Elige una opción:\n1. Leer lista-1\n2. Salir-2\n")
    if opcion == "1":
        print(lectura())
    elif opcion == "2":
        salir()
    else:
        print("Opción no válida")
        return menu(input("Elige una opción:\n1. Leer lista-1\n2. Salir-2\n"))
    
menu()
