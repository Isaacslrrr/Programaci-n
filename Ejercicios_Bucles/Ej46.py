#46. A partir del programa anterior, soluciona el error que se produce en el test anterior con la 
#palabra Abrigo utilizando únicamente una instrucción.

palabra=input("Introduce una palabra: ")
var1=[]
var2=[]

vocales="aeiouAEIOU"

for letra in palabra:
    if letra in vocales:
        var1.append(letra)
    else:
        var2.append(letra)
print(var1, "vocales")
print(var2, "consonantes")