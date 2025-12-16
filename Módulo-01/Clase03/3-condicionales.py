#Calculadora

#Entrada
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación a realizar(+,-) :")

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