# Los datos compuestos son tipos de datos que ṕueden almacenar múltiples valores

# Lista (list) #

"""
Caracteristicas:

Almacena datos repetidos
Tienen un orden fijo
Se puede modificar los elementos
Se puede acceder al elemento por su índice
"""

lista1 = ["Hola", 10, 10.5, True, False, None, ["Dato compuesto", "Otro elemento", ["Dajachi"]]]
print(lista1)

# Acceder a un elemento de la lista por su índice
print(lista1[-1])

# Crear una lista con la funcion list()
lista2 = list(["David", 16])
print(lista2)

# Modificar un elemento
lista1[0] = "Dajachi"
print(lista1)

# Acceder a un rango de elementos (slicign)
# [inicio:fin:paso]
lista = [10, 20, 30, 40, 50]
print(lista[1:4])  # (20, 30, 40) (elementos desde el índice 1 hasta el 3)
print(lista[::2])  # (10, 30, 50) (elementos con un paso de 2)


# Tupla (tuple) #

"""
Caracteristicas:

Almacena datos repetidos
Tienen un orden fijo
No se puede modificar los elementos
Se puede acceder al elemento por su índice
"""

tupla1 = ("Pedro", 16, 15.8, True, False, ["Pera", "Banano"], False)
print(tupla1[1])

# Modificar los elementos (esto esta mal)
#tupla1[0] = "David"
#print(tupla1)

# Crear una tupla con la función tuple()
tupla2 = tuple(["Elemento1", "Elemento2"])
print(tupla2)


# Crear una tupla con un solo elemento
tupla3 = 43,
print(type(tupla3))


# Conjunto (set) #

"""
Caracteristicas:

No Almacena datos repetidos
No Tienen un orden fijo
No se puede modificar los elementos
no Se puede acceder al elemento por su índice
Solo se puede accder a los elementos por medio del bucle for
"""

conjunto1 = {"Dajachi", "David", 10, 10.6, True, False, "Dajachi"}

# No se puede modificar un elemento
#conjunto1[0] = "David"
#print(conjunto1)


# No se accede al elemento por su índice
#print(conjunto1[0])


# Diccionario (dict) #

"""
Caracteristicas:

La estructura es: clave: valor y se separa por comas
Almacena datos repetidos
Tienen un orden fijo
Se puede modificar los elementos
Se puede accede al valor por su clave
"""

dic = {
    "Nombre": "David",
    "Edad": 16,
    "Programando": True,
    "Lenguajes": ["Python", "HTMl", "CSS", "JavaScript", "MySQL"]
}

# Accder al valor por su clave
print(dic["Lenguajes"])

# Modificar el valor
dic["Lenguajes"] = ["Python", "HTML", "CSS"]
print(dic)