# Todo el texto en mayúscula upper()
texto1 = "hello, my name is David and I like to program in python"
print(texto1.upper())

# Todo en minuscula lower()
texto1 = "HELLO, MY NAME IS DAVID AND I LIKE TO PROGRAM IN PYTHON"
print(texto1.lower())

# Primera en mayúscula con title()
texto1 = "hello, my name is David and I like to program in Python"
print(texto1.capitalize())

# Primera de todas las palabras en mayucula con capitalize()
texto1 = "hello, my name is David and I like to program in Python"
print(texto1.title())

# Eliminar espacios de una cadena con strip()
texto = "   Python  "
print(texto.strip())
print(texto.lstrip())
print(texto.rstrip())

# Buscar un elmento en una cadena con find, devuelve el índice de la primera ocurrencia, sino devuelve -1
texto1 = "I like to program in Python"
print(texto1.find("to")) # 7

# Buscar un elemento en una cadena con index, devuelve el índice de la primera ocurrencia, sino devuelve una exepción
texto1 = "I like to program in Python"
print(texto1.index("I")) # 0

# Remplazar un elemento por otro con replace()
texto = "Hola Mundo"
print(texto.replace("Mundo", "Python"))  # "Hola Python"

# split() - Divide una cadena en una lista separada por un delimitador
texto = "manzana-pera-uva"
print(texto.split("-"))

# Unir elementos de una lista en una sola cadena
lista = ["Hola", "Mundo"]
print(" ".join(lista)) # "Hola Mundo"

# Verifica si una cadena empieza o termina con un valor específico.
texto = "programacion.py"
print(texto.startswith("pro"))  # True
print(texto.endswith(".py"))    # True

# Contar cuántas veces aparece una subcadena dentro de otra
texto = "python python python"
print(texto.count("python")) # 3

# .isnumeric(): Verifica si solo contiene números.
# .isalpha(): Verifica si solo contiene letras.
# .isalnum(): Verifica si solo contiene letras y números.

texto1 = "123"
texto2 = "Python"
texto3 = "Python123"

print(texto1.isnumeric())  # True
print(texto2.isalpha())    # True
print(texto3.isalnum())    # True
