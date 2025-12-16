#Bucle FOR
for contador in range(4):
    print(contador)

#Tabla de multiplicar
tabla = int(input("Ingrese la tabla de multiplicar que desea ver: "))
for contador in range(1,13,1):
    resultado = tabla * contador
    print(f"{tabla} x {contador} = {resultado}")