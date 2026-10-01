edad = int(input("Ingrese su edad: "))

if edad > 0 and edad < 220:
    numpulsaciones = (220 - edad) / 10
    print("Número de pulsaciones por cada 10 segundos:", numpulsaciones)
else:
    print("Error: Ingrese una edad válida.")