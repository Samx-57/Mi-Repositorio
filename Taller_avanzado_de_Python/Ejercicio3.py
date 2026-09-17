while True:
    numero = int(input("Ingrese un número entero mayor que 1: "))
    if numero > 1:
        break
    print("Error: El número debe ser mayor que 1.")

divisores = []
for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)

print("Divisores:", divisores)

if len(divisores) == 2:
    print("El número", numero, "es primo.")
else:
    print("El número", numero, "no es primo.")