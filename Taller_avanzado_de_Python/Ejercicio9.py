pares = 0
impares = 0
mayores = 0

i = 1
while i <= 10:
    print("TABLA DEL ", i)
    j = 1
    while j <= 10:
        res = i * j
        print(i, " por ", j, " = ", res)
        if res % 2 == 0:
            pares = pares + 1
        else:
            impares = impares + 1
        if res > 50:
            mayores = mayores + 1
        j = j + 1
    print()
    i = i + 1

print("Pares: ", pares)
print("Impares: ", impares)
print("Mayores a 50: ", mayores)