print("Ingrese las notas del estudiante entre 0.0 y 5.0")
a=float(input("Ingrese la primera nota: "))
b=float(input("Ingrese la segunda nota: "))
c=float(input("Ingrese la tercera nota: "))
d=float(input("Ingrese la cuarta nota: "))
e=float(input("Ingrese la quinta nota: "))
prom=(a+b+c+d+e)/5
if prom<3.5:
    print("Usted saco ", prom, " en el promedio de notas por lo que reprobo el curso")
else:
    print("Usted saco ", prom, " en el promedio de notas por lo que aprobo el curso")