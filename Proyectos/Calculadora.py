# Programa que simula una calculadora (En desarrollo)

import tkinter as tk

root = tk.Tk()
root.title("Calculadora")
root.configure(bg="#6A5ACD")

resultado = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="groove", bg="#E6E6FA", fg="#000000")
resultado.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

fila = 1
col = 0

botones = [
    'C',  # Botón de borrado
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
        except Exception:
            resultado.delete(0, tk.END)
            resultado.insert(0, "Error")
    else:
        resultado.insert(tk.END, boton)

# Función para limpiar la entrada
def clear():
    resultado.delete(0, tk.END)

# Creando los botones de la calculadora
for boton in botones:
    tk.Button(root, text=boton, width=7, height=3, command=lambda b=boton: click(b) if b != 'C' else clear(), bg="#8A2BE2", fg="#FFFFFF", font=('Arial', 18)).grid(row=fila, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        fila += 1

root.mainloop()
