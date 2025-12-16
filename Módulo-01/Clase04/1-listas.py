dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

# mostrar info de la lista

print(dias[0])  # Imprime "Lunes"

# agregar elementos de la lista
dias.append("Sábado")
dias.append("Domingo")

# eliminar elementos de la lista
dias.pop(2)  # Elimina "Miércoles"
del dias[0:2]

# actualizar elementos de la lista
dias[-1] = "Lunes"

# mostrar todos los elementos de la lista
for dia in dias:
    print(dia)