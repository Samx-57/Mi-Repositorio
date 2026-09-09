def buscar_producto(inventario, codigo):
  for prod in inventario:
    if prod[0] == codigo:
      return prod
  return None


def valor_total(inventario):
  total = 0
  for prod in inventario:
    precio = prod[2]
    cantidad = prod[3]
    total = total + (precio * cantidad)
  return total


def actualizar_stock(inventario, codigo, nueva_cantidad):
  for i in range(len(inventario)):
    if inventario[i][0] == codigo:
      prod_lista = list(inventario[i])
      prod_lista[3] = nueva_cantidad
      inventario[i] = tuple(prod_lista)
      return True
  return False


inventario = [
    ("001", "Computador", 2000000, 3),
    ("002", "Mouse", 50000, 10),
    ("003", "Teclado", 120000, 5),
]

print("Inventario actual:")
print("Código   Nombre     Precio     Cantidad     Valor Total")
for prod in inventario:
  codigo = prod[0]
  nombre = prod[1]
  precio = prod[2]
  cantidad = prod[3]
  valor_item = precio * cantidad
  print(codigo, "   ", nombre, "   ", precio, "   ", cantidad, "   ", valor_item)

print()
print("Valor total del inventario: $", valor_total(inventario))