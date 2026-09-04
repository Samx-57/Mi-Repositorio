
# Ejercicio 3. Compra en una tienda.

producto = str(input("Ingrese el nombre del producto: "))
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad de productos: "))

total = float(precio * cantidad)

print("======= FACTURA ========")
print("Producto: " + producto)
print("Precio: " + str(precio))
print("Cantidad: " + str(cantidad))
print("Total a pagar: $" + str(total))
