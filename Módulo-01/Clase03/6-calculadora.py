#Calculadora completa con Python

salir = "no"
while(salir == "no"):
    salir = input("Desea salir? (si/no): ")
    if salir == "si":
        break
    #Entrada
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación a realizar(+,-,x,/) :")

    #Procesamiento
    if operacion =="+":
        resultado = numero1 + numero2
    elif operacion =="-":
        resultado = numero1 - numero2
    elif operacion =="x":
        resultado = numero1 * numero2
    elif operacion =="/":
        resultado = numero1 / numero2
    else:
        print("Operación no válida")
        exit()

    #Salida
    print(f"{numero1} {operacion} {numero2} = {resultado}")