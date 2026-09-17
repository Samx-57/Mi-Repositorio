while True:
    cantidad_productos = int(input("Ingrese la cantidad de productos comprados: "))
    if cantidad_productos > 0:
        break
    print("Error: La cantidad debe ser mayor a cero.")

subtotal_general = 0
total_descuentos = 0
detalles_productos = []

for i in range(cantidad_productos):
    print("\nProducto", i + 1, ":")
    nombre = input("Nombre del producto: ")
    
    while True:
        precio = float(input("Precio unitario: ").replace(",", "."))
        cantidad = int(input("Cantidad comprada: "))
        if precio > 0 and cantidad > 0:
            break
        print("Error: El precio y la cantidad deben ser mayores a cero.")
        
    print("Tipo de producto (1: alimento, 2: aseo, 3: otro)")
    tipo = input("Seleccione el tipo (1/2/3): ")
    
    subtotal_producto = precio * cantidad
    subtotal_general = subtotal_general + subtotal_producto
    
    descuento_producto = 0
    
    if tipo == "1":
        descuento_producto = subtotal_producto * 0.05
    elif tipo == "2":
        if cantidad >= 3:
            descuento_producto = subtotal_producto * 0.10
    
    total_descuentos = total_descuentos + descuento_producto
    total_producto = subtotal_producto - descuento_producto
    
    detalles_productos.append({
        "nombre": nombre,
        "subtotal": subtotal_producto,
        "descuento": descuento_producto,
        "total": total_producto
    })

descuento_adicional = 0
if subtotal_general > 300000:
    descuento_adicional = subtotal_general * 0.05
    total_descuentos = total_descuentos + descuento_adicional

total_definitivo = subtotal_general - total_descuentos

print("\n--- FACTURA DE SUPERMERCADO ---")
for prod in detalles_productos:
    print("Producto:", prod["nombre"])
    print("  Subtotal:", prod["subtotal"])
    print("  Descuento aplicado:", prod["descuento"])
    print("  Total producto:", prod["total"])

print("\nTotal antes del descuento general:", subtotal_general)
if descuento_adicional > 0:
    print("Descuento adicional por superar $300.000 (5%):", descuento_adicional)
print("Total de descuentos:", total_descuentos)
print("Total definitivo a pagar:", total_definitivo)