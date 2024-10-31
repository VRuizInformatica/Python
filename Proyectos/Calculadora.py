# Programa que simula una calculadora (En desarrollo)
import os  # Importa el módulo os para interactuar con el sistema operativo
import tkinter as tk  # Importa tkinter para crear la interfaz gráfica
import sqlite3  # Importa sqlite3 para manejar la base de datos SQLite

# Conexión a la base de datos y creación de la tabla historial si no existe
con = sqlite3.connect('Historial.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS historial (id INTEGER PRIMARY KEY AUTOINCREMENT, operacion TEXT, resultado TEXT)''')
con.commit()

# Definición de colores y fuentes para la interfaz
BG_COLOR = "#7F00FF"
ENTRY_BG = "#E6E6FA"
BUTTON_BG = "#8A2BE2"
BUTTON_FG = "#FFFFFF"
FONT = ('Sans', 18)
INSTRUCTION_FONT = ('Arial', 12)
TITLE_COLOR = "#4B0082"

# Función para evaluar expresiones matemáticas
def evaluate_expression(expression):
    try:
        # Manejo de porcentajes en la expresión
        if '%' in expression:
            parts = expression.split('%')
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                expression = f"({parts[0]}/100)*{parts[1]}"
        
        result = str(eval(expression))  # Evalúa la expresión
        con = sqlite3.connect('Historial.db')  # Nueva conexión a la base de datos
        cur = con.cursor()
        
        # Inserta la operación y el resultado en la base de datos
        cur.execute("INSERT INTO historial (operacion, resultado) VALUES (?, ?)", (expression, result))
        con.commit()
        con.close()

        return result  # Devuelve el resultado
    except Exception:
        return "Error"  # Manejo de errores

# Función para manejar clics en los botones
def handle_button_click(button):
    current_text = resultado.get()  # Obtiene el texto actual del campo de entrada
    
    if button == '=':
        result = evaluate_expression(current_text)  # Evalúa la expresión
        resultado.delete(0, tk.END)  # Limpia el campo de entrada
        resultado.insert(0, result)  # Muestra el resultado
    elif button == 'C':
        clear()  # Limpia el campo de entrada
    elif button == '√':
        try:
            resultado_final = str(eval(f"({current_text})**0.5"))  # Calcula la raíz cuadrada
            resultado.delete(0, tk.END)
            resultado.insert(0, resultado_final)
        except Exception:
            resultado.delete(0, tk.END)
            resultado.insert(0, "Error")  # Manejo de errores
    elif button == '^':
        resultado.insert(tk.END, '**')  # Inserta el operador de potencia
    else:
        # Manejo de la entrada de números y operadores
        if button == '0':
            if current_text == '' or current_text[-1] in ['+', '-', '*', '/']:
                resultado.insert(tk.END, '0.')  # Evita múltiples ceros
            else:
                resultado.insert(tk.END, button)
        elif button == '.':
            if current_text == '' or current_text == '0':
                resultado.delete(0, tk.END)
                resultado.insert(tk.END, '0.')  # Manejo del punto decimal
            elif '.' not in current_text.split()[-1]:
                resultado.insert(tk.END, button)
        else:
            resultado.insert(tk.END, button)  # Inserta el botón presionado

# Función para limpiar el campo de entrada
def clear():
    resultado.delete(0, tk.END)

# Función para eliminar el último carácter del campo de entrada
def delete_last_character():
    current_text = resultado.get()
    resultado.delete(0, tk.END)
    resultado.insert(0, current_text[:-1])  # Elimina el último carácter

# Función para mostrar instrucciones de uso
def show_instructions():
    instrucciones_ventana = tk.Toplevel(root)  # Crea una nueva ventana
    instrucciones_ventana.title("Instrucciones")

    # Etiquetas con instrucciones
    tk.Label(instrucciones_ventana, text="Instrucciones de uso de la calculadora:", font=('Arial', 14, 'bold'), fg=TITLE_COLOR).pack(pady=10)
    tk.Label(instrucciones_ventana, text="1. Introducción de operaciones:", font=INSTRUCTION_FONT, fg=TITLE_COLOR).pack(anchor='w', padx=10)
    tk.Label(instrucciones_ventana, text="   - Escribe la operación que deseas realizar en el campo de entrada.").pack(anchor='w', padx=20)
    tk.Label(instrucciones_ventana, text="   - Puedes usar números operadores matemáticos y el botón '%' para porcentajes.").pack(anchor='w', padx=20)

    tk.Label(instrucciones_ventana, text="2. Cálculo de porcentajes:", font=INSTRUCTION_FONT, fg=TITLE_COLOR).pack(anchor='w', padx=10)
    tk.Label(instrucciones_ventana, text="   - Para calcular un porcentaje utiliza la sintaxis 'X%Y', donde 'X' es el porcentaje y 'Y' es el total.").pack(anchor='w', padx=20)
    tk.Label(instrucciones_ventana, text="   - Por ejemplo '7%100' calculará el 7% de 100.").pack(anchor='w', padx=20)

    tk.Label(instrucciones_ventana, text="3. Obtener resultados:", font=INSTRUCTION_FONT, fg=TITLE_COLOR).pack(anchor='w', padx=10)
    tk.Label(instrucciones_ventana, text="   - Presiona el botón '=' para obtener el resultado de la operación ingresada.").pack(anchor='w', padx=20)

    tk.Label(instrucciones_ventana, text="4. Limpiar la entrada:", font=INSTRUCTION_FONT, fg=TITLE_COLOR).pack(anchor='w', padx=10)
    tk.Label(instrucciones_ventana, text="   - Utiliza el botón 'C' para limpiar el campo de entrada y comenzar de nuevo.").pack(anchor='w', padx=20)

    tk.Label(instrucciones_ventana, text="5. Información adicional:", font=INSTRUCTION_FONT, fg=TITLE_COLOR).pack(anchor='w', padx=10)
    tk.Label(instrucciones_ventana, text="   - Presiona el botón 'Info' para volver a ver estas instrucciones en cualquier momento.").pack(anchor='w', padx=20)

    instrucciones_ventana.update_idletasks()
    instrucciones_ventana.minsize(300, 200)  # Establece el tamaño mínimo de la ventana

# Función para mostrar el historial de operaciones
def show_history():
    historial_ventana = tk.Toplevel(root)  # Crea una nueva ventana
    historial_ventana.title("Historial de Operaciones")
    
    # Crea un directorio para la base de datos si no existe
    if not os.path.exists(os.getcwd() + '/DB'):
        os.mkdir(os.getcwd() + '/DB')

    con = sqlite3.connect('Historial.db')  # Conexión a la base de datos
    cur.execute("SELECT operacion, resultado FROM historial")  # Selecciona las operaciones y resultados
    rows = cur.fetchall()  # Obtiene todas las filas
    con.close()
    
    # Muestra cada operación y su resultado en la ventana
    for row in rows:
        tk.Label(historial_ventana, text=f"{row[0]} = {row[1]}", font=INSTRUCTION_FONT, fg=TITLE_COLOR).pack(anchor='w', padx=10)

    historial_ventana.update_idletasks()
    historial_ventana.minsize(300, 200)  # Establece el tamaño mínimo de la ventana

# Configuración de la ventana principal
root = tk.Tk()
root.title("Calculadora")
root.configure(bg=BG_COLOR)

# Campo de entrada para mostrar resultados
resultado = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="groove", bg=ENTRY_BG, fg="#4B0082")
resultado.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Botón para mostrar el historial
tk.Button(root, text="Historial", width=7, height=2, command=show_history, bg=BUTTON_BG, fg=BUTTON_FG, font=FONT).grid(row=0, column=3, padx=5, pady=5)

# Creación de botones para la calculadora
buttons = ['C', '^', '%', '√', '+', '7', '8', '9', '-', '4', '5', '6', '*', '1', '2', '3', '/', '0','.','=']
for i, button in enumerate(buttons):
    tk.Button(root, text=button, width=7, height=3, command=lambda b=button: handle_button_click(b), bg=BUTTON_BG, fg=BUTTON_FG, font=FONT).grid(row=(i // 4) + 1, column=i % 4, padx=5, pady=5)

root.mainloop()  # Inicia el bucle principal de la interfaz gráfica