"""
UPPER() - Todo en mayuscúla
LOWER() - Todo en minuscúla
TITLE() - Primera en mayuscúla
CAPITALIZE() - Primera de todas las palabras en mayuscúla
STRIP() - Eliminar todos los espacios de una cadena
LSTRIP() - Eliminar los espacios al incio de una cadena
RSTRIP() - Eliminar los espacios al final de una cadena
FIND() - Devuelve el índice de la primera ocurrencia, sino devuelve -1
INDEX() - Devuelve el índice de la primera ocurrencia, sino devuelve una exepción
REPLACE() - Remplaza un elemento por otro
SPLIT() - Separa la cadena en una lista
STARTSWITH() - Verifica si la cadena empieza con
ENDSWITH() - Verifica si la cadena termina con
COUNT() - Cuenta las veces que se repite el valor dado
ISNUMERIC() - Verifica si la cadena contiene números
ISALPHA() - Verifica si la cadena es solo letras
ISALNUM() - Verifica si la cadena contiene letras y números
"""

# Métodos de cadenas
# Al aplicar un método a una cadena, no modifica la original

# upper()
cadena1 = "hola mundo"
print(cadena1.upper())

# lower()
cadena2 = "HOLA MUNDO"
print(cadena2.lower())

# title() - Primera de todas las palabras en mayuscúla
print(cadena1.title())

# capitalize() - Primera en mayuscúla
print(cadena1.capitalize())

# strip() - Eliminar todos los espacios de la cadena 
cadena3 = "    hola mundo    "
print(cadena3.strip())

# find() - devuelve el índice de la primera ocurrencia, sino devuelve -1
print(cadena1.find("m"))

# index() - devuelve el índice de la primera ocurrencia, sino devuelve una exepción
print(cadena1.index("m"))

# replace() - Remplazar un valor por otro
print(cadena1.replace("mundo", "python"))

# split() - separa las cadenas en una lista
lista = cadena1.split()
print(lista)

# startswith() - verificar si la cadena inicia con
print(cadena1.startswith("h"))

# endswith() - verificar si termina con
print(cadena1.endswith("o"))

# count() - cuenta las veces que se repite un valor un una cadena 
print(cadena1.count("o"))

# isalpha() - verificar si la cadena es solo es letras (si la cadena contiene espacios, devuelve False)
print(cadena1.isalpha())

# isnumric() - verificar si la cadena contiene números
print(cadena1.isnumeric())

cadena4 = "david123"

# isalnum() - verifica si la cadena contiene letras y números
print(cadena4.isalnum())