import random

class PokemonCard:
    def __init__(self, nombre, tipo, hp, ataque, defensa, habilidadEspecial):
        self.nombre = nombre
        self.tipo = tipo
        self.hp = hp
        self.ataque = ataque
        self.defensa = defensa
        self.habilidadEspecial = habilidadEspecial
        self.bool = True
    
    def atacar(self, defensor):
        daño = self.ataque - defensor.defensa
        if random.randint(1, 4) == 1 and self.bool:
            self.bool = False
            self.habilidad_Especial()
        if daño > 0:
            defensor.recibirDaño(daño)
        else:
            print(f"¡Qué defensa de {defensor.nombre}!")

    def habilidad_Especial(self):
        self.ataque += (self.ataque * 20) // 100
        print(f"El ataque de {self.nombre} ha aumentado un 20%: {self.ataque}")

    def recibirDaño(self, daño):
        self.hp -= daño
        print(f"La vida de {self.nombre} ha disminuido a {self.hp}")
        if self.hp <= 0:
            print(f"{self.nombre} está fuera de combate!")

class BattleSimulator:
    def batalla(Pokemon1, Pokemon2):
        while Pokemon1.hp > 0 and Pokemon2.hp > 0:
            Pokemon1.atacar(Pokemon2)
            if Pokemon2.hp <= 0:
                print(f"¡{Pokemon1.nombre} gana la batalla!")
                break
            Pokemon2.atacar(Pokemon1)
            if Pokemon1.hp <= 0:
                print(f"¡{Pokemon2.nombre} gana la batalla!")
                break

Torterra = PokemonCard("Torterra", "Planta", 100, 30, 20, "Hoja Afilada")
Gengar = PokemonCard("Gengar", "Fantasma", 90, 40, 10, "Bola Sombra")

BattleSimulator.batalla(Torterra, Gengar)
