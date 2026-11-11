a=int(input("Ingrese el valor de a: "))
b=int(input("Ingrese el valor de b: "))
c=int(input("Ingrese el valor de c: "))
dis=(b**2)-(4*a*c)
if a!=0 and dis>=0:
    print("La ecuacion cuadratica tiene solucion")
else:
    print("La ecuacion cuadratica no tiene solucion")