#Conversor de moneda

tipo_cambio = 3.5 # Soles por Dólar

def soles_a_dolares(soles):
    """Convierte una cantidad de Soles a Dólares."""
    return soles / tipo_cambio

def dolares_a_soles(dolares):
    """Convierte una cantidad de Dólares a Soles."""
    return dolares * tipo_cambio

print("Bienvenido al convertidor de moneda!")
print("1. Convertir Soles a Dólares")
print("2. Convertir Dólares a Soles")

opcion_elegida = input("Por favor, elija una opción (1 o 2): ")

if opcion_elegida == '1':
    try:
        cantidad_soles = float(input("Ingrese la cantidad en Soles: "))
        dolares_convertidos = soles_a_dolares(cantidad_soles)
        print(f"{cantidad_soles:.2f} Soles son {dolares_convertidos:.2f} Dólares")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número para la cantidad.")
elif opcion_elegida == '2':
    try:
        cantidad_dolares = float(input("Ingrese la cantidad en Dólares: "))
        soles_convertidos = dolares_a_soles(cantidad_dolares)
        print(f"{cantidad_dolares:.2f} Dólares son {soles_convertidos:.2f} Soles")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número para la cantidad.")
else:
    print("Opción no válida. Por favor, elija 1 o 2.")