class Ajedrez:
    tablero = [
        ["T", "C", "A", "D", "R", "A", "C", "T"],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        ["t", "c", "a", "d", "r", "a", "c", "t"]
    ]

    # Función para imprimir el tablero
    def imprimir_tablero(tablero):
        for fila in tablero:
            print(" ".join(fila))

    imprimir_tablero(tablero)