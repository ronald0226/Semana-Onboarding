precio= float(input("ingrese el precio de la compra: $"))
if precio < 0:
    print ("precio no valido")
elif precio >200000:
    descuento= precio * 0.20
    print("descuento del 20%")
    print("total a pagar", precio - descuento)
elif precio >100000:
    descuento= precio * 0.10
    print("descuento del 10%")
    print("total a pagar", precio - descuento)
else:
    print("sin descuento")
    print("total a pagar", precio)