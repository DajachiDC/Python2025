
# Teoría de conjuntos

conjunto1 = {"a", "b", "c"}
conjunto2 = {"a", "b", "d", "c"}

# verificar si el conjunto1 es un sub-conjunto de conjunto2
print(conjunto1.issubset(conjunto2)) # True

# verificar si el conjunto2 es un sub-conjunto de conjunto1
print(conjunto2.issubset(conjunto1)) # False

# verificar con operador de comparacion <=
print(conjunto1 <= conjunto2) # True

# verificar sin conjunto2 es un superconjunto de conjunto1
print(conjunto2.issuperset(conjunto1)) # True