cantidad_total = 0
positivos = 0
negativos = 0
pares = 0
impares = 0
suma_total = 0
numero_mayor = None
numero_menor = None

primer_numero = True

while True:
    numero = int(input("Ingrese un número entero (0 para terminar): "))
    if numero == 0:
        break
    
    if primer_numero:
        numero_mayor = numero
        numero_menor = numero
        primer_numero = False
    else:
        if numero > numero_mayor:
            numero_mayor = numero
        if numero < numero_menor:
            numero_menor = numero
            
    cantidad_total = cantidad_total + 1
    suma_total = suma_total + numero
    
    if numero > 0:
        positivos = positivos + 1
    elif numero < 0:
        negativos = negativos + 1
        
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

if cantidad_total == 0:
    print("No se ingresaron números (el primero fue 0).")
else:
    promedio = suma_total / cantidad_total
    print("\n--- ESTADÍSTICAS ---")
    print("Cantidad de números ingresados:", cantidad_total)
    print("Cantidad de positivos:", positivos)
    print("Cantidad de negativos:", negativos)
    print("Cantidad de pares:", pares)
    print("Cantidad de impares:", impares)
    print("Suma total:", suma_total)
    print("Promedio:", promedio)
    print("Número mayor:", numero_mayor)
    print("Número menor:", numero_menor)