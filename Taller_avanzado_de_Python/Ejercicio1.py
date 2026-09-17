while True:
    lado1 = float(input("Ingrese el lado 1: ").replace(",", "."))
    lado2 = float(input("Ingrese el lado 2: ").replace(",", "."))
    lado3 = float(input("Ingrese el lado 3: ").replace(",", "."))
    
    if lado1 > 0 and lado2 > 0 and lado3 > 0:
        break
    print("Error: Todos los lados deben ser mayores a cero.")

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Sí es un triángulo válido.")
    
    if lado1 == lado2 and lado2 == lado3:
        print("Clasificación: Equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Clasificación: Isósceles")
    else:
        print("Clasificación: Escaleno")
else:
    print("No se puede formar un triángulo con las medidas ingresadas.")