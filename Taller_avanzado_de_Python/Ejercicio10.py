while True:
    n = int(input("Ingrese un número entre 3 y 10: "))
    if 3 <= n <= 10:
        break
    print("Error: El número debe estar entre 3 y 10.")

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

for i in range(n - 1, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()