valor=int(input("Ingrese el valor del articulo para ver si aplica al descuento sin puntos ni comas: "))
if valor>=150000:
    b=valor*0.05
    print("El producto aplica para un descuento del 5% por lo tanto su valor queda en $",valor-b,)
else:
    print("El producto no aplica para un descuento por lo tanto su valor es $",valor)