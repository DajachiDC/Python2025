dict1 = {
    "Nombre": "David",
    "Apellido": "Jaramillo",
    "Edad": 16,
    "Apodo": "Dajachi",
    "Lenguaje": "Python"
}
print(dict1)

# Obtener todas las claves con keys()
print(dict1.keys())

# Obtener todos los valores con values()
print(dict1.values())

# Obtener el valor de una clave
print(dict1.get("Apodo"))

# Eliminar un elemento
dict1.pop("Lenguaje")
print(dict1)

# Iterar el dict (devuelve  una tupla con cada clave, valor)
for i in dict1.items():
    print(f"{i[0]}: {i[1]}")


# Eliminar todos los elementos del dict
dict1.clear()
print(dict1)