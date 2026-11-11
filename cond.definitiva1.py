a=float(input("Ingrese la nota definitiva entre 0.0 a 5.0: "))
if a<3.0:
    print("Insuficiente")
elif a<=3.5:
    print("Aceptable")
elif a<=4.0:
    print("Sobresaliente")
else:
    print("Excelente")