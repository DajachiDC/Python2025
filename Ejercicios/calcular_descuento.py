def calcular_descuento(precio_original, descuento):
    return precio_original - (precio_original * descuento / 100)


precio_original = 100
descuento = 15
precio_final = calcular_descuento(precio_original, descuento)
print(f"El precio final con {descuento}% de descuento es {precio_final}")