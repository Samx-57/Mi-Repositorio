
# RETOS PRACTICOS
# Reto 1. Nomina basica

print("============ RETO 1 =============")

nombre_empleado = str(input("ingrese el nombre del empleado: "))
horas_trabajadas = int(input("ingrese las horas trabajadas: "))
valor_hora = float(input("ingrese el valor de la horas de trabajo: "))

salario = horas_trabajadas * valor_hora

print("Empleado: " + nombre_empleado)
print("Horas trabajadas: " + str(horas_trabajadas))
print("Valor hora: " + str(valor_hora))
print("Salario: $" + str(salario))

print("==========================") 
print("========== RETO 2 ===========")

nombre_cliente = str(input("Ingrese el nombre del cliente: "))
valor_comida = float(input("ingrese el valor de la comida: "))
valor_bebidas = float(input("ingrese el valor de la bebida: "))

subtotal = valor_comida + valor_bebidas
propina = subtotal * 0.10
total = subtotal + propina

print("Nombre del cliente: " + nombre_cliente)
print("Valor de la comida: $" + str(valor_comida))
print("Valor de las bebidas: $" + str(valor_bebidas))
print("propina: $" + str(propina))
print("Total a pagar: $" + str(total))

print("==============================")
print("============ RETO 3 =============")
nombre_ = str(input("ingrese su nombre: "))
peso_kg = float(input("ingrese su peso en kg: "))
estatura = float(input("ingrese su estatura en metros: "))

imc = peso_kg / estatura ** 2

print("Nombre: " + nombre_)
print("Peso: " + str(peso_kg))
print("Altura: " + str(estatura))
print("IMC: " + str(imc))

print("============================")
print("=========== RETO 4 ============")

codigo_equipo = int(input("ingrese el codigo del equipo: "))
marca = str(input("Ingrese la marca: "))
procesador = str(input("ingrese el procesador: "))
ram = int(input("ingrese la memoria RAM: "))
capacidad_disco = float(input("ingrese la capacidad del disco: "))
so = str(input("ingrese el sistema operativo: "))
estado = str(input("ingrese el estado del equipo: "))

print("======= FICHA TECNICA DEL EQUIPO =======")
print("========================================")
print("Codigo del equipo: " + str(codigo_equipo))
print("Marca: " + str(marca))
print("Procesador: " + str(procesador))
print("Memoria RAM: " + str(procesador))
print("Capacidad del disco: " + str(capacidad_disco))
print("Sistema operativo: " + str(so))
print("Estado del equipo: " + str(estado))

print("=========================================")

print("==== 4. RETO INTEGRADOR ====")
# SISTEMA BASICO DE MATRICULA UNIVERSITARIA

codigo = input("Ingrese el código del estudiante: ")
nombre = input("Ingrese el nombre completo: ")
edad = int(input("Ingrese la edad: "))
programa = input("Ingrese el programa académico: ")
semestre = int(input("Ingrese el semestre: "))
materias = int(input("Ingrese el número de materias: "))
valor_materia = float(input("Ingrese el valor de cada materia: "))

total = materias * valor_materia

print("Registro de matrícula")
print("Código:", codigo)
print("Estudiante:", nombre)
print("Edad:", edad)
print("Programa:", programa)
print("Semestre:", semestre)
print("Materias:", materias)
print("Valor por materia:", valor_materia)
print("Total matrícula:", total)

print("=====================================")
print("====== Actividad de analisis =======")

#1 El problema es que input() guarda la edad como texto y no como número, entonces Python no puede sumar directamente 5 a ese texto.
#2 Devuelve un dato de tipo str, osea texto.
#3 Se puede convertir la edad a entero usando int().

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

nueva_edad = edad + 5

print(nombre)
print(nueva_edad)