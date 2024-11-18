#10. Introduce por teclado dos números y muestre por pantalla la siguiente información: 
#cociente, resto y si el dividendo es par o impar.

var1=float(input("Introduce un valor :"))
var2=float(input("Introduce otro valor :"))

var3=var1/var2
var4=var1%var2

print("El cociente es:", var3)
print("El resto es:", var4)
if var2%2==0:
    print("El dividendo es par")
else:
    print("El dividendo es impar")
