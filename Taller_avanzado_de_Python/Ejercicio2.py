while True:
    cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
    if cantidad_estudiantes > 0:
        break
    print("Error: La cantidad debe ser mayor a cero.")

aprobados = 0
reprobados = 0
suma_total_grupo = 0
promedio_mas_alto = -1
promedio_mas_bajo = 6

for i in range(cantidad_estudiantes):
    print(f"\nEstudiante {i + 1}:")
    
    while True:
        nota1 = float(input("Ingrese la nota 1 (0.0 a 5.0): ").replace(",", "."))
        nota2 = float(input("Ingrese la nota 2 (0.0 a 5.0): ").replace(",", "."))
        nota3 = float(input("Ingrese la nota 3 (0.0 a 5.0): ").replace(",", "."))
        
        if (0.0 <= nota1 <= 5.0) and (0.0 <= nota2 <= 5.0) and (0.0 <= nota3 <= 5.0):
            break
        print("Error: Las notas deben estar entre 0.0 y 5.0.")
    
    promedio_estudiante = (nota1 + nota2 + nota3) / 3
    suma_total_grupo = suma_total_grupo + promedio_estudiante
    
    if promedio_estudiante <= 2.9:
        clasificacion = "Reprobado"
        reprobados = reprobados + 1
    elif promedio_estudiante <= 3.9:
        clasificacion = "Aprobado"
        aprobados = aprobados + 1
    elif promedio_estudiante <= 4.5:
        clasificacion = "Sobresaliente"
        aprobados = aprobados + 1
    else:
        clasificacion = "Excelente"
        aprobados = aprobados + 1
        
    print(f"Promedio: {promedio_estudiante:.2f} - Clasificación: {clasificacion}")
    
    if promedio_estudiante > promedio_mas_alto:
        promedio_mas_alto = promedio_estudiante
        
    if promedio_estudiante < promedio_mas_bajo:
        promedio_mas_bajo = promedio_estudiante

promedio_general_grupo = suma_total_grupo / cantidad_estudiantes

print("\n--- REPORTE FINAL ---")
print("Cantidad de estudiantes aprobados:", aprobados)
print("Cantidad de estudiantes reprobados:", reprobados)
print(f"Promedio general del grupo: {promedio_general_grupo:.2f}")
print(f"Promedio más alto: {promedio_mas_alto:.2f}")
print(f"Promedio más bajo: {promedio_mas_bajo:.2f}")