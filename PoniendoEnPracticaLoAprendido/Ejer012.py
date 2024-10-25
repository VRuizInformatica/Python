# Programa que simula una cuenta bancaria

import os

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def get_cantidad(self):
        return self.cantidad

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
        else:
            print("No se puede ingresar una cantidad negativa.")

    def retirar(self, cantidad):
        if cantidad < 0:
            print("No se puede retirar una cantidad negativa.")
            exit
        if self.cantidad - cantidad < 0:
            self.cantidad = 0
        else:
            self.cantidad -= cantidad

    def guardar_saldo(self):
        with open("saldo.txt", "w") as f:
            f.write(str(self.cantidad))

    def cargar_saldo(self):
        if os.path.exists("saldo.txt"):
            with open("saldo.txt", "r") as f:
                self.cantidad = float(f.read())

mi_cuenta = Cuenta("Victor")
mi_cuenta.cargar_saldo()  # Cargar saldo al iniciar

respuesta = input("Buenos dias, ¿que desea hacer hoy (ingresar(i), retirar(r), consultar saldo(c))? \n").lower()

if respuesta == "ingresar" or respuesta == "i":
    cantidad = float(input("Introduzca la cantidad que desea ingresar:\n"))
    mi_cuenta.ingresar(cantidad)
    mi_cuenta.guardar_saldo()  # Guardar saldo después de ingresar
    print(f"Nuevo saldo: {mi_cuenta.get_cantidad()}€")

elif respuesta == "retirar" or respuesta == "r":
    cantidad = float(input("¿Cuanto desea retirar?\n"))
    mi_cuenta.retirar(cantidad)
    mi_cuenta.guardar_saldo()  # Guardar saldo después de retirar
    print(f"Nuevo saldo: {mi_cuenta.get_cantidad()}€")

elif respuesta == "consultar" or respuesta == "c":
    print(f"Saldo actual: {mi_cuenta.get_cantidad()}€")

else:
    print("Introduzca ingresar, retirar, consultar o en su atajo i, r, c.")
