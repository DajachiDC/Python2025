# Porcentaje de un número

def calcular_porcentaje(numero, porcentaje):
    return (numero * porcentaje) / 100


numero = 100
porcentaje = 25

resultado = calcular_porcentaje(numero, porcentaje)
print(f"{porcentaje}% de {numero} es: {resultado}")