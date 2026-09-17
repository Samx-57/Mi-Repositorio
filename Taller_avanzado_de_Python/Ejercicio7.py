while True:
    numero = int(input("Ingrese un número entero positivo: "))
    if numero >= 0:
        break
    print("Error: El número debe ser positivo o cero.")

if numero == 0:
    binario = "0"
else:
    binario = ""
    aux = numero
    while aux > 0:
        residuo = aux % 2
        binario = binario + str(residuo)
        aux = aux // 2

print("Número decimal:", numero)
print("Resultado binario:", binario)