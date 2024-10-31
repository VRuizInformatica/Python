# Programa que invierte una palabra

# Solicita al usuario que ingrese una frase y almacena la entrada en la variable 'respuesta'
respuesta = input("Voy a invertir tus palabras prueba \n")

# Elimina los espacios en blanco de la cadena ingresada
respuesta = respuesta.replace(" ", "")

# Imprime la cadena invertida utilizando el slicing
print ((respuesta)[::-1])
