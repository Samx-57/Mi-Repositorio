capital = float(input("Ingrese el capital a invertir: "))

if capital > 0:
    interesmensual = 0.15 / 12
    ganancia = capital * interesmensual
    total = capital + ganancia
    print("Ganancia en un mes:", ganancia)
    print("Dinero total:", total)
else:
    print("Error: El capital debe ser mayor a cero.")