# las tuplas son inmutables
dias = ("lunes", "martes", "miércoles", "jueves", "viernes")
print(f"Tipo de dato original : {type(dias)}")
dias = list(dias)
print(f"Tipo de dato modificado : {type(dias)}")
dias.append("sábado") # Esto genera un error porque las tuplas son inmutables
dias = tuple(dias)

print(dias)