pesos = float(input("Ingrese la cantidad en pesos: "))
tasa = float(input("Ingrese el valor actual del dólar: "))

if pesos > 0 and tasa > 0:
    dolares = pesos / tasa
    print("La equivalencia en dólares es:", dolares)
else:
    print("Error: Los valores deben ser mayores a cero.")