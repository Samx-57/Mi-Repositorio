totalcompra = float(input("Ingrese el total de la compra: "))

if totalcompra > 0:
    descuento = totalcompra * 0.15
    totalfinal = totalcompra - descuento
    print("El total a pagar con el 15% de descuento es:", totalfinal)
else:
    print("Error: El valor debe ser mayor a cero.")