import random

print("1. Fácil (1-20, 6 intentos)")
print("2. Intermedio (1-50, 5 intentos)")
print("3. Difícil (1-100, 4 intentos)")

while True:
    opcion = input("Nivel (1/2/3): ")
    if opcion == "1":
        limite = 20
        intentos = 6
        break
    elif opcion == "2":
        limite = 50
        intentos = 5
        break
    elif opcion == "3":
        limite = 100
        intentos = 4
        break

secreto = random.randint(1, limite)
gano = False

for i in range(intentos):
    intento = int(input("Número: "))
    if intento == secreto:
        print("Número correcto")
        print("Puntaje:", (intentos - i) * 20)
        gano = True
        break
    elif intento < secreto:
        print("El número secreto es mayor")
    else:
        print("El número secreto es menor")

if not gano:
    print("Era:", secreto)
    print("Puntaje: 0")