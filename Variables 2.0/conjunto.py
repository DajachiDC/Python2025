
# Crear un conjunto con set()
conjunto = set(["dato1", "dato2"])
print(conjunto)

# metiendo un ocnjunto dentro de otro conjunto
conjunto1 = frozenset({"dato1", "dato2"}) # frozenset() convierte un objeto iterable en un conjunto inmutable
conjunto2 = {conjunto1, "dato3"}
print(conjunto2)

# Teoría de conjuntos

conjunto_a = {"a", "b", "c"}
conjunto_b = {"a", "b", "c", "d"}

# verificar si es subconjunto
resultado = conjunto_b.issubset(conjunto_a)
print(resultado)

resultado = conjunto_b <= conjunto_a
print(resultado)

# Verificar si es un superconjunto
conjunto_a = {"a", "b", "c"}
conjunto_b = {"a", "b", "c", "d"}

resultado = conjunto_b.issuperset(conjunto_a)
print(resultado)