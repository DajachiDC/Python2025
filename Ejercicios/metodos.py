# Ejercicio 1: Eliminar duplicados de una lista

lista = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sin_duplicados = list(set(lista))
print(sin_duplicados)


# Ejercico 2: Filtrar números pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#numeros_pares = [num for num in numeros if num % 2 == 0]
#print(numeros_pares)

numeros_pares = []
for num in numeros:
    if num % 2 == 0:
        numeros_pares.append(num)
    
print(numeros_pares)