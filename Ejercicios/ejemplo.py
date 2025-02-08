congelador = [("tomate", 100)]
print(congelador)

nombre = "tomate"

for elemento in congelador:
    if elemento[0] == nombre:
        congelador.remove(elemento)

print(congelador)