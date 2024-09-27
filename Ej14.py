#14. Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área 
#y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el 
#resultado a un decimal.

var1=float(input("Introduc el diámetro de un círculo :"))

import math

var2=var1/2
var3=math.pi*var2**2
var4=2*math.pi*var2
var5=round(var3, 1)
var6=round(var4, 1)

print("El área es", var5)
print("El perímetro es", var6)
