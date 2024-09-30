#7. programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes 
#forzar que el resultado de la división tenga 2 decimales?

var1=float(input("Introduce el primer valor :"))
var2=float(input("Introduce el seguundo valor :"))

var3=var2+var1
var4=var1-var2
var5=var1*var2
var7=var1**var2
var8=var1//var2

print("la suma es :", var3)
print("la resta es :", var4)
print("la multiplicación es :", var5)
print("la división es :", round(var1/var2, 2))
print("el exponente es :", var7)
print("la división entera es :", var8)
