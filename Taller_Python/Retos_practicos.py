
print("======RETO 1========")
nombre_cliente = input("Digite el nombre del cliente: ")
precio_comida = float(input("Digite el precio de la comida: "))
precio_bebida = float(input("Digite el precio de la bebida: "))
cantidad_personas = int(input("Digite la cantidad de personas: "))

total_cuenta = precio_comida + precio_bebida
valor_por_persona = total_cuenta / cantidad_personas

print("Cliente:", nombre_cliente)
print("Total de la cuenta:", total_cuenta)
print("Valor por persona:", valor_por_persona)

print("======RETO 2========")

celsius = float(input("Digite la temperatura en grados Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperatura en Fahrenheit:", fahrenheit)

print("=====RETO 3=======")

pesos = float(input("Digite la cantidad en pesos: "))
valor_dolar = float(input("Digite el valor actual del dólar: "))

total_dolares = pesos / valor_dolar

print("Cantidad en dólares:", total_dolares)

print("======RETO 4=======")

nombre_cliente = input("Digite el nombre del cliente: ")
producto = input("Digite el producto: ")
precio = float(input("Digite el precio unitario: "))
cantidad = int(input("Digite la cantidad: "))

subtotal = precio * cantidad
iva = subtotal * 0.19
total = subtotal + iva

print("------ FACTURA ------")
print("Cliente:", nombre_cliente)
print("Producto:", producto)
print("Cantidad:", cantidad)
print("Precio unitario:", precio)
print()
print("Subtotal:", subtotal)
print("IVA:", iva)
print("TOTAL:", total)

print("=======RETO FINAL========")

vendedor = input("Digite el nombre del vendedor: ")
cliente = input("Digite el nombre del cliente: ")
producto = input("Digite el producto: ")
cantidad = int(input("Digite la cantidad: "))
precio_unitario = float(input("Digite el precio unitario: "))

subtotal = precio_unitario * cantidad
descuento = subtotal * 0.10
subtotal_con_descuento = subtotal - descuento
iva = subtotal_con_descuento * 0.19
total_final = subtotal_con_descuento + iva

print("========= VENTA =========")
print("Vendedor:", vendedor)
print("Cliente:", cliente)
print("Producto:", producto)
print("Cantidad:", cantidad)
print()
print("Subtotal: $" + str(int(subtotal)))
print("Descuento: $" + str(int(descuento)))
print("IVA: $" + str(int(iva)))
print()
print("TOTAL A PAGAR: $" + str(int(total_final)))