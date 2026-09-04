
# Ejercicio 7. Compra en una tienda:

nombre_producto = str(input("nombre del producto: "))
precio = float(input("precio: "))
cantidad = int(input("Cantidad: "))

subtotal = precio * cantidad

print("Producto: " + nombre_producto)
print("Precio: " + str(precio))
print("Cantidad: " + str(cantidad))
print("Total: $" + str(subtotal))
