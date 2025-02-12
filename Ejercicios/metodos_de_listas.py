# Contar la cantida de elementos que tiene una cadena
lista1 = ["Python", "HTML", "CSS", "JavaScript"]
print(len(lista1))


# Agregar un elemento al final de la lista con append()
lista1.append("Go")
print(lista1)

# Agregar un elemento a la lista en un índice especifico
lista1.insert(1, "Java")
print(lista1)

# Agregar varios elementos a una lista
lista1.extend(["SQL", "PHP"])
print(lista1)

# Eliminar un elemento con pop() (Pide el índice del elmento y devuelve el valor)
print(lista1.pop(-1))
print(lista1)

# Eliminar un elemento por su valor
lista1.remove("Go")
print(lista1)

# Ordenar la lista de menor a mayor
lista2 = [2, 1, 4, 3, 8, 7, 6, 5]
lista2.sort() # con el parametro 'reverse=True' le da la vuelta a la lista
print(lista2)

# Dar la vuelta a la lista
lista2.reverse()
print(lista2)

# Limpiar la lista con clear()
lista1.clear()
print(lista1)