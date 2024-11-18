#12. Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor 
#y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.

var1=float(input("Introduce el valor de un lado de un trapecio isósceles :"))
var2=float(input("Introduce el valor de la base menor de un trapecio isósceles :"))
var3=float(input("Introduce el valor de la base mayor de un trapecio isósceles :"))
var4=float(input("Introduce el valor de la altura de un trapecio isósceles :"))

var5=var1*2
var6=var2+var3+var5
var7=var2+var3
var8=var7/2
var9=var8*var4

print("El perimetro es", var6)
print("El área es", var9)
