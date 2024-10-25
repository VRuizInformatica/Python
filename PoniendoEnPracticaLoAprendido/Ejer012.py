# Programa que simula una cuenta bancaria

class Cuenta:
    # Inicializa la cuenta con un titular y una cantidad opcional
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    # Devuelve la cantidad actual en la cuenta
    def get_cantidad(self):
        return self.cantidad

    # Permite ingresar una cantidad a la cuenta
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
        else:
            print("No se puede ingresar una cantidad negativa.")

    # Permite retirar una cantidad de la cuenta
    def retirar(self, cantidad):
        if cantidad < 0:
            print("No se puede retirar una cantidad negativa.")
            exit
        if self.cantidad - cantidad < 0:
            self.cantidad = 0
        else:
            self.cantidad -= cantidad


# Se crea una instancia de la cuenta con un titular y un saldo inicial
mi_cuenta = Cuenta("Victor", 100.0)

# Solicita al usuario qué acción desea realizar
respuesta = input("Buenos dias, ¿que desea hacer hoy (ingresar(i), retirar(r), consultar saldo(c))? \n").lower()

# Maneja la opción de ingresar dinero
if respuesta == "ingresar" or respuesta == "i":
    cantidad = float(input("Introduzca la cantidad que desea ingresar:\n"))
    mi_cuenta.ingresar(cantidad)
    print(f"Nuevo saldo: {mi_cuenta.get_cantidad()}€")

# Maneja la opción de retirar dinero
elif respuesta == "retirar" or respuesta == "r":
    cantidad = float(input("¿Cuanto desea retirar?\n"))
    mi_cuenta.retirar(cantidad)
    print(f"Nuevo saldo: {mi_cuenta.get_cantidad()}€")

# Maneja la opción de consultar el saldo
elif respuesta == "consultar" or respuesta == "c":
    print(f"Saldo actual: {mi_cuenta.get_cantidad()}€")

# Maneja la entrada no válida
else:
    print("Introduzca ingresar, retirar, consultar o en su atajo i, r, c.")
