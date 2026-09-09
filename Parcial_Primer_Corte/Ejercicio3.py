ventas = {
    "enero": [1200, 1500, 800, 900],
    "febrero": [1000, 1100, 1200],
    "marzo": [1800, 1700, 1600, 2000]
}

def total_mes(ventas, mes):
    suma = 0
    for valor in ventas[mes]:
        suma = suma + valor
    return suma

def promedio_general(ventas):
    suma_total = 0
    cantidad_total = 0
    for mes in ventas:
        for valor in ventas[mes]:
            suma_total = suma_total + valor
            cantidad_total = cantidad_total + 1
    return suma_total / cantidad_total

def mejor_mes(ventas):
    mayor_total = -1
    nombre_mejor_mes = ""
    for mes in ventas:
        total_actual = total_mes(ventas, mes)
        if total_actual > mayor_total:
            mayor_total = total_actual
            nombre_mejor_mes = mes
    return nombre_mejor_mes

def filtrar_ventas_altas(ventas, limite):
    altas = []
    for mes in ventas:
        for valor in ventas[mes]:
            if valor >= limite:
                altas.append(valor)
    return altas

limite_usuario = float(input("Ingrese el límite de ventas a filtrar: ").replace(",", "."))

total_enero = total_mes(ventas, "enero")
total_febrero = total_mes(ventas, "febrero")
total_marzo = total_mes(ventas, "marzo")
promedio = promedio_general(ventas)
top_mes = mejor_mes(ventas)
ventas_filtradas = filtrar_ventas_altas(ventas, limite_usuario)

print()
print("Total por mes:")
print("Enero:", total_enero)
print("Febrero:", total_febrero)
print("Marzo:", total_marzo)
print()
print("Promedio general trimestral:", promedio)
print("Mejor mes:", top_mes)
print("Ventas mayores al límite ingresado:", ventas_filtradas)