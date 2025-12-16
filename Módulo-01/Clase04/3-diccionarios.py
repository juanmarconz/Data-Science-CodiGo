# Diccionarios
# Son colecciones desordenadas de elementos que se almacenan en pares clave-valor.
# Cada clave es única y se utiliza para acceder a su valor correspondiente.
# Se definen utilizando llaves {} y los pares clave-valor se separan por comas.

capitales = {
    "Perú": "Lima",
    "Ecuador": "Quito",
    "Colombia": "Bogotá",
    "Argentina": "Buenos Aires",
}

# Acceder a un valor mediante su clave
print(capitales["Ecuador"])  # Imprime "Quito"

# Agregar o modificar un nuevo par clave-valor
capitales["Chile"] = "Santiago"
nueva_capital = {
    "Bolivia": "La Paz"
}

capitales.update(nueva_capital)
print(capitales)

# Eliminar un par clave-valor
del capitales["Argentina"]
capital_eliminada = capitales.pop("Ecuador","No encontrada")
print(f"Se eliminó la capital {capital_eliminada}.")
print(capitales)

# Recorrer un diccionario
print("Recorriendo el diccionario de capitales:")
# Por claves
for clave in capitales.keys():
    print(clave)

# Por valores
for valor in capitales.values():
    print(valor)
    
# Por clave-valor
for clave, valor in capitales.items():
    print(f"La capital de {clave} es {valor}") 
