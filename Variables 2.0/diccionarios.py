# Crear un diccionario con dict() - La unica forma de crear un diccionario sin contendio es con dict()
dic = dict(nombre="David", apodo="Dajachi")
print(dic)

# Las listas no pueden ser claves y se usa frozenset para meter conjuntos
#diccionario = {["Apodo"]: "Dajachi"} - No se puede
diccionario = {("Apodo"): "Dajachi"}
print(diccionario[("Apodo")])

# Creando diccionarios con fromkeys() valor por defecto: None
diccionario = dict.fromkeys(["nombre", "apodo"])
print(diccionario)

# Cambiar el valor por defecto a "apodo"
# Creando diccionarios con fromkeys() (El primer dato es un iterable y el segundo a lo que se va a igualar)
diccionario = dict.fromkeys("nombre", "apodo")
print(diccionario)