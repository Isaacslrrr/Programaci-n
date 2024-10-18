#17. Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el 
#peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado 
#es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso.

var1=float(input("Introduce tu peso en kg :"))
var2=float(input("Introduce tu altura en metros :"))

var3=var1/var2**2

if var3>25:
    print("Tu IMC es:", var3,".Tienes sobrepeso")
else:
    print("Tu IMC es:", var3,".No tienes sobrepeso")
    
 
