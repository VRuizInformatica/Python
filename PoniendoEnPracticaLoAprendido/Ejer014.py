# Crear un programa que muestre los números pares del 1 al 100

def lista():
    # Inicializa una lista vacía para almacenar los números pares
    listaDef = []
    # Itera a través de los números del 1 al 100
    for i in range(1, 101):
        # Verifica si el número es par
        if i % 2 == 0:
            # Agrega el número par a la lista
            listaDef = listaDef + [i]
    # Devuelve la lista de números pares
    return listaDef

def lectura():
    # Llama a la función lista() y devuelve su resultado
    return(lista())

def salir():
    # Imprime un mensaje de despedida y termina el programa
    print("Hasta luego")
    exit()

def menu():
    # Solicita al usuario que elija una opción
    opcion = input("Elige una opción:\n1. Leer lista-1\n2. Salir-2\n")
    # Si elige la opción 1, imprime la lista de números pares
    if opcion == "1":
        print(lectura())
    # Si elige la opción 2, llama a la función salir()
    elif opcion == "2":
        salir()
    # Si la opción no es válida, informa al usuario y vuelve a mostrar el menú
    else:
        print("Opción no válida")
        return menu(input("Elige una opción:\n1. Leer lista-1\n2. Salir-2\n"))
    
# Llama a la función menu() para iniciar el programa
menu()
