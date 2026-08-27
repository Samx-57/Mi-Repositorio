
#Ejercicio 6. Calculadora de edad.

nombre = str(input("ingrese su nombre: "))
año_de_nacimiento = int(input("ingrese su año de nacimiento: "))
año_actual = int(input("ingrese el año actual: "))

edad_aprox = año_actual - año_de_nacimiento

print(nombre + " tiene aproximadamente " + str(edad_aprox) + "  años.")