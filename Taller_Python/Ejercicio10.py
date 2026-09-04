
# Ejercicio 10. Salario de un trabajador.

nombre = str(input("Ingrese su nombre: "))
horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
valorXhora = float(input("Ingrese el valor por hora: "))

salario = float(horas_trabajadas * valorXhora)
print("===========================")

print("Empleado: " + nombre)
print("Salario: $" + str(salario))
