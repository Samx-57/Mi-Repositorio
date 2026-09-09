estudiantes = []


def agregar_estudiante(lista):
  nombre = input("Nombre: ")
  edad = int(input("Edad: "))
  nota = float(input("Nota: ").replace(",", "."))
  estudiante = {"nombre": nombre, "edad": edad, "nota": nota}
  lista.append(estudiante)


def promedio_notas(lista):
  suma = 0
  for est in lista:
    suma = suma + est["nota"]
  return suma / len(lista)



def mejor_estudiante(lista):
  mejor = lista[0]
  for est in lista:
    if est["nota"] > mejor["nota"]:
      mejor = est
  return mejor


while True:
  agregar_estudiante(estudiantes)
  continuar = input("¿Desea agregar otro estudiante? (si/no): ")
  if continuar.lower() != "si":
    break

total = len(estudiantes)
promedio = promedio_notas(estudiantes)
mejor = mejor_estudiante(estudiantes)

print()
print("Total estudiantes:", total)
print("Promedio general:", promedio)
print(
    "Mejor estudiante:",
    mejor["nombre"],
    "-",
    mejor["nota"],
    "-",
    mejor["edad"],
)