opcion = 0
cantidad_ventas = 0
total_bruto = 0
total_descuentos = 0
total_recargos = 0
total_recibido = 0

venta_mayor = 0
cliente_mayor = ""
venta_menor = 0
cliente_menor = ""

pagos_efectivo = 0
pagos_tarjeta = 0
pagos_transferencia = 0
clientes_descuento = 0

while opcion != 5:
    print("\n1. Registrar una venta")
    print("2. Consultar resumen de ventas")
    print("3. Consultar venta mayor y menor")
    print("4. Aplicar cierre de caja")
    print("5. Salir")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        cliente = input("Nombre del cliente: ")
        while True:
            cantidad_productos = int(input("Cantidad de productos: "))
            if cantidad_productos > 0:
                break

        subtotal_venta = 0
        for i in range(cantidad_productos):
            while True:
                precio = float(input(f"Precio del producto {i + 1}: ").replace(",", "."))
                if precio > 0:
                    break
            subtotal_venta = subtotal_venta + precio

        while True:
            medio = input("Medio de pago (1: Efectivo, 2: Tarjeta, 3: Transferencia): ")
            if medio in ["1", "2", "3"]:
                break

        descuento_diez = subtotal_venta * 0.10 if subtotal_venta > 500000 else 0
        descuento_tres = subtotal_venta * 0.03 if medio == "1" and subtotal_venta > 200000 else 0
        recargo = subtotal_venta * 0.02 if medio == "2" else 0
        
        descuento_total = descuento_diez + descuento_tres
        total_final = subtotal_venta - descuento_total + recargo

        cantidad_ventas = cantidad_ventas + 1
        total_bruto = total_bruto + subtotal_venta
        total_descuentos = total_descuentos + descuento_total
        total_recargos = total_recargos + recargo
        total_recibido = total_recibido + total_final

        if medio == "1":
            pagos_efectivo = pagos_efectivo + 1
        elif medio == "2":
            pagos_tarjeta = pagos_tarjeta + 1
        else:
            pagos_transferencia = pagos_transferencia + 1

        if descuento_total > 0:
            clientes_descuento = clientes_descuento + 1

        if cantidad_ventas == 1 or total_final > venta_mayor:
            venta_mayor = total_final
            cliente_mayor = cliente
        if cantidad_ventas == 1 or total_final < venta_menor:
            venta_menor = total_final
            cliente_menor = cliente

        print("Total a pagar:", total_final)

    elif opcion == 2 or opcion == 4:
        if cantidad_ventas == 0:
            print("No hay ventas registradas.")
        else:
            print("\n--- RESUMEN Y CIERRE ---")
            print("Cantidad de ventas:", cantidad_ventas)
            print("Valor total bruto:", total_bruto)
            print("Total de descuentos:", total_descuentos)
            print("Total de recargos:", total_recargos)
            print("Dinero recibido:", total_recibido)
            print("Promedio de ventas:", total_recibido / cantidad_ventas)
            print("Pagos en efectivo:", pagos_efectivo)
            print("Pagos con tarjeta:", pagos_tarjeta)
            print("Pagos por transferencia:", pagos_transferencia)
            print("Clientes con descuento:", clientes_descuento)

    elif opcion == 3:
        if cantidad_ventas == 0:
            print("No hay ventas registradas.")
        else:
            print("\n--- VENTA MAYOR Y MENOR ---")
            print("Venta mayor:", cliente_mayor, "con", venta_mayor)
            print("Venta menor:", cliente_menor, "con", venta_menor)

    elif opcion == 5:
        print("Programa finalizado.")
    else:
        print("Opción inválida.")