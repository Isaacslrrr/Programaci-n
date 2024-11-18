#21. Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz 
#cuadrada no de un valor negativo
import math

var1=float(input("Introduce el primer valor de una ecuación de 2do grado :"))
var2=float(input("Introduce el segundo valor de una ecuación de 2do grado, ha de ser negativo:"))
var3=float(input("Introduce el tercer valor de una ecuación de 2do grado :"))

r1=((var2**2)-(4*var1*var3))
if r1>0:
    x1=((-var2)+math.sqrt(r1))/2*var1
    x2=((-var2)-math.sqrt(r1))/2*var1
    print("El valor de x1 es", x1)
    print("El valor de x2 es", x2)
#resultado 2 = r2#

else:
     print("La raíz no puede ser un valor negativo")


