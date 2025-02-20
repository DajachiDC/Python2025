animales = ["perro", "gato", "loro", "cocodrilo"]
numeros = [1,2,3,4]

# recorriendo la lista animales
for animal in animales:
    print(f"Ahora la variable animal es igual a: {animal}")
    
    
# recorriendo la lista números
for numero in numeros:
    resultado = numero * 10
    print(resultado)
    
    

# Iterar dos o más listas del mismo tamaño al mismo tiempo con zip()
for animal,numero in zip(animales, numeros):
    print(f"{numero}: {animal}")
    
    
# Iterar con range()
for num in range(1,11):
    print(num)
    

# Forma correcta de recorrer una lista con enumerate()
# devuelve una tupla con el índice y el valor
for indice, animal in enumerate(animales):
    print(f"El índice es: {indice} y el valor es: {animal}")


# Usando el for/else - Se ejecuta siempre una sola vez despues de que termine el bucle
for numero in numeros:
    print(numero)

else:
    print("El bucle termino")
    
# todo lo anterior funciona exactamente igual para las tuplas