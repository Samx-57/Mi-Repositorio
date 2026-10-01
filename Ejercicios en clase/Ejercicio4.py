p1 = float(input("Nota parcial 1: "))
p2 = float(input("Nota parcial 2: "))
p3 = float(input("Nota parcial 3: "))
examen = float(input("Nota examen final: "))
trabajo = float(input("Nota trabajo final: "))

if p1 >= 0 and p2 >= 0 and p3 >= 0 and examen >= 0 and trabajo >= 0:
    promedioparciales = (p1 + p2 + p3) / 3
    calificacionfinal = (promedioparciales * 0.40) + (examen * 0.50) + (trabajo * 0.10)
    print("Su calificación final en Algoritmos es:", calificacionfinal)
else:
    print("Error: Las notas no pueden ser negativas.")