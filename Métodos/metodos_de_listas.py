"""
LIST() - Crea una lista

LEN() - Devuelve la cantidad de elementos de una lista

APPEND - Agrega un elemento a la lista
INSERT - Agrega un elemento a la lista en el índice especifico
EXTEND - Agrega varios elmentos a la lista

POP - Elimina un elemento de una lista, pide índice y devuelve el valor
REMOVE - Remueve un elemento de una lista, pide valor
CLEAR - Elimina todos los elementos de una lista

SORT - Ordena una lista de forma ascendente a descendente
REVERSE - Invierte los elementos de una lista
"""

# Crear una lista con list() (uso: crear listas vacias)
list = list(["Dajachi", 16, "DajachiCode"])

lista = ["David", "Dajachi", "Python", "Programación", 16, True, False]

# Función len() (Devuelve la cantidad de elementos de una lista)
print(len(lista))

# Agregar elementos a la lista con append()
lista.append("HTML")
print(lista)

# Agregar un elemento a la lista en un índice especifico
lista.insert(0, "DajachiCode")
print(lista)

# Agregar un elemento a la lista con extend()
lengaujes = ["Python", "HTML", "CSS"]
print(lengaujes)
lengaujes.extend(["JavaScript", "MySQL", "Ruby", "Go"])
print(lengaujes)


# Eliminar un elemento de la lista con pop() por su índice
print(lengaujes.pop(3))
lengaujes.pop(-1) # Eliminar el ultimo elemento de la lista
print(lengaujes)

# Eliminar un elemento de la lista con remove() por su valor
lengaujes.remove("Ruby")
print(lengaujes)

# Eliminar todos los elementos de la lista con clear()
lengaujes.clear()
print(lengaujes)


# Ordenar la lista de manera ascendente a descendente
letras = ["b", "c", "a", "e", "d"]
print(letras)
letras.sort(reverse=True) # reverse=True (con el parametro reverse los ordena en reversa)
print(letras)

lista1 = [6,5,4,3,2,1, True, False]
lista1.sort()
print(lista1)

# Dar la vuelva a la cadena con reverse()
letras = [1,2,3,4,5,6,7,8,9,10]
letras.reverse()
print(letras)