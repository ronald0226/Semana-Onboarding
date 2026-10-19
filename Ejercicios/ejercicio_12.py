lado1= float(input("ingrese el primer lado"))
lado2= float(input("ingrese el segundo lado"))
lado3= float(input("ingrese el tercer lado"))
if lado1 <=0 or lado3 <=0 or lado2 <=0:
    print("lados no validos")
elif lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
    print ("el triangulo es invalido")
elif lado1 == lado2 and lado2 ==lado3:
    print("el triangulo es equilatero")
elif lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
    print("el triangulo es isosceles")
else:
    print("el triangulo es escaleno")