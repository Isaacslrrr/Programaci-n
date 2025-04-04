#39. Programa que pida n números y que, tras introducir el último número, debe aparecer por 
#pantalla el número total de positivos, negativos y número de 0.

positivo=0
negativo=0

var1=int(input("Cuantos números deseas introducir: "))
for i in range(var1):
    var2=int(input("Introducelo: "))
    if var2<0:
        negativo+=1
    else:
        positivo+=1
        
print(negativo, "negativos")
print(positivo, "positivos")