while True:
    cantidad = int(input("Ingrese la cantidad de términos: "))
    if cantidad > 0:
        break
    print("Error: La cantidad debe ser mayor a cero.")

serie = []

for i in range(cantidad):
    if i == 0:
        serie.append(0)
    elif i == 1:
        serie.append(1)
    else:
        siguiente = serie[i - 1] + serie[i - 2]
        serie.append(siguiente)

suma = 0
pares = 0
impares = 0

for numero in serie:
    suma = suma + numero
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print("La serie completa:", serie)
print("La suma de sus términos:", suma)
print("Cuántos términos son pares:", pares)
print("Cuántos términos son impares:", impares)