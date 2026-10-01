sueldobase = float(input("Ingrese el sueldo base: "))
venta1 = float(input("Valor de la primera venta: "))
venta2 = float(input("Valor de la segunda venta: "))
venta3 = float(input("Valor de la tercera venta: "))

if sueldobase >= 0 and venta1 >= 0 and venta2 >= 0 and venta3 >= 0:
    totalventas = venta1 + venta2 + venta3
    comision = totalventas * 0.10
    sueldototal = sueldobase + comision
    print("Comisión por las tres ventas:", comision)
    print("Total a recibir en el mes:", sueldototal)
else:
    print("Error: Los valores no pueden ser negativos.")