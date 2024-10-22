# Programa que simula una calculadora(En desarrollo)

import tkinter as tk

root = tk.Tk()
root.title("Calculadora")

resultado = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="groove")
resultado.grid(row=0, column=0, columnspan=4)

fila = 1
col = 0

botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

def click(boton):
    if boton == '=':
        try:
            expresion = resultado.get()
            resultado_final = str(eval(expresion))
            resultado.delete(0, tk.END)
            resultado.insert(0, resultado_final)
        except Exception as e:
            resultado.delete(0, tk.END)
            resultado.insert(0, "Error")
    else:
        resultado.insert(tk.END, boton)

for boton in botones:
    tk.Button(root, text=boton, width=5, height=2, command=lambda b=boton: click(b)).grid(row=fila, column=col)
    col += 1
    if col > 3:
        col = 0
        fila += 1

root.mainloop()
