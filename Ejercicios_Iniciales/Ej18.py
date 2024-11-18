#18. Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan 
#importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores 
#de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por 
#teclado el número de menores y el número de adultos que asisten al cine.

var1=float(input("Introduce el número de menores que asisten al cine :"))
var2=float(input("Introduce el número de adultos que asisten al cine :"))

var3=50*12/100
var4=10*12/100

var5=var1*12-var3*var1
var6=var2*12-var4*var2

print("El precio total del cine para", var1, "menor/es es", var5)
print("El precio total del cine para", var2, "adulto/s es", var6)
