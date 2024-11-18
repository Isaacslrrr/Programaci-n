#19. Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son 
#iguales

var1=float(input("Introduce un valor :"))
var2=float(input("Introduce un valor :"))

if var1>var2:
    print(var1, "es mayor a", var2)
elif var1==var2:
    print(var1, "es igual a", var2)
else:
    print(var2, "es mayor a", var1)