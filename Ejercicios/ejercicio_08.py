nota= float(input("ingrese la nota (0 a 100): "))
if nota < 0 or nota > 100:
    print("nota no valida")
elif nota >= 70:
    print("estudiante aprobado")
else:
    print("estudiante reprobado")