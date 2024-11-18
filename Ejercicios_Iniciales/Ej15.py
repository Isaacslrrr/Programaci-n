#15. Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, 
#introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.

var1=float(input("introduce el valor de el radio de un cilindro :"))
var2=float(input("introduce el valor de la altura de un cilindro :"))

import math

var3=2*math.pi*var1*var2
var4=math.pi*var1**2
var5=2*var4+var3
var6=math.pi*var1**2*var2
var7=round(var5, 2)
var8=round(var6, 2)

print("El área es", var7)
print("El volumen es", var8)
