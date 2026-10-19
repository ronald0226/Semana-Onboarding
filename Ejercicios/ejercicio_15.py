cliente = input("ingrese el nombre del cliente: ")
producto = input("ingrese el nombre del producto: ")
precio = float(input("ingrese el precio del producto: "))
cantidad = int(input("ingrese la cantidad: "))
subtotal = precio * cantidad
if precio < 0 or cantidad <= 0:
    print("precio o cantidad no validos")
else:
    if subtotal >= 500000:
        descuento = subtotal * 0.15
    elif subtotal >= 200000:
        descuento = subtotal * 0.10
    else:
        descuento = 0

    total = subtotal - descuento
    print ("-------FACTURA------")
    print ("cliente:", cliente)  
    print ("producto", producto)
    print ("precio", precio)
    print ("cantidad", cantidad)
    print ("subtotal", subtotal)
    print ("descuento", descuento)
    print ("total a pagar", total)          
