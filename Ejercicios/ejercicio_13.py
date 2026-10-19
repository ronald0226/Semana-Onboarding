print ("CALCULADORA")
print ("1. Sumar")
print ("2. Restar")
print ("3. multiplicar")
print ("2. Dividir")
opcion=input("seleccione un opcion:")

num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingese el segundo numero: "))
if opcion == "1":
    print ("Resultado:", num1 + num2)
elif opcion == "2":
    print ("Resultado:", num1 - num2)
elif opcion == "3":
    print("Resultado:", num1 *num2)
elif opcion == "4":
    if num2 !=0:
        print("Resultado:",num1 / num2)
    else:
        print("no se puede dividir entre cero")
else:
    print("pocion no valida")