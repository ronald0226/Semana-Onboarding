num1= float(input("ingrese el primer numero"))
num2=float(input("ingrese el segundo numero"))
operacion = input("ingrese la operacion")
if operacion == "+":
    print("la suma es:", num1 + num2)
    
elif operacion == "-" :
    print("la resta es:", num1 - num2)

elif operacion == "*" :
    print ("la multiplicacion es:", num1 * num2)
elif operacion == "/" :
    if num2 !=0:
        print("la division es:", num1 / num2)

    else:
        print("no se puede dividir entre cero")