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


mi_cuenta = Cuenta("Victor", 100.0)

respuesta = input("Buenos dias, ¿que desea hacer hoy (ingresar, retirar, consultar saldo)? \n").lower()

if respuesta == "ingresar":
    cantidad = float(input("Introduzca la cantidad que desea ingresar:\n"))
    mi_cuenta.ingresar(cantidad)
    print(f"Nuevo saldo: {mi_cuenta.get_cantidad()}€")

elif respuesta == "retirar":
    cantidad = float(input("¿Cuanto desea retirar?\n"))
    mi_cuenta.retirar(cantidad)
    print(f"Nuevo saldo: {mi_cuenta.get_cantidad()}€")

elif respuesta == "consultar":
    print(f"Saldo actual: {mi_cuenta.get_cantidad()}€")

else:
    print("Introduzca ingresar, retirar o consultar.")
