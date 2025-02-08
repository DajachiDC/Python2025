"""
keys() -> devuelve las claves (también sirve para iterar)
get() -> devuelve el valor de una clave
clear() -> elimina todos los elementos
pop() -> elimina un elemento y devuelve el valor
items() -> para iterar el dict
"""

diccionario = {
    "nombre": "David",
    "apellido": "Jaramillo",
    "edad": 16
}

print(diccionario.keys())

#diccionario["adasd"] # Devuelve un error
print(diccionario.get("apellido")) # Sino lo encuentra no devuelve errores

diccionario.pop("edad")
print(diccionario)

# obtener un elemento dict_items iterable
diccionario_iterable = diccionario.items()
print(diccionario_iterable)

# Eliminar todo del diccionario
diccionario.clear()
print(diccionario)