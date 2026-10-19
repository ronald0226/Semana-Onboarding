print ("CAJERO AUTOMATICO")
print ("1.consultar saldo")
print ("2.retirar dinero")
print ("3.salir")
opcion= input("seleccione una opcion")
saldo = 1000000
if opcion == "1":
    print("su saldo es", saldo)
elif opcion == "2":
    retiro=float(input("ingrese el valor a retirar: "))
    if retiro <=0:
        print("valor no valido")
    elif retiro > saldo:
        print("saldo insuficiente")
    else:
        saldo = saldo - retiro
        print("Retiro exitoso")
        print("saldo actual")

elif opcion =="4":
    print("gracias por utilizar el cajero")
