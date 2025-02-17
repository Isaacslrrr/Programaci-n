#62. Realiza un programa que pida dos números por teclado y presente por pantalla qué números 
#hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo.


var1=int(input("Introduce un valor: "))
var2=int(input("Introduce un valor: "))
var3=0

concatenarpar=""
concatenarimpar=""

if var1>var2:
    var3=var1
    var2=var1
    var2=var3

for recorrer in range(var1, var2+1):
    if recorrer%2==0:
        concatenarpar+=str(recorrer)+"-"
        
    else:
        concatenarimpar+=str(recorrer)+"-"
 
concatenaropar=concatenarpar[:-1]
concatenaroimpar=concatenarimpar[:-1]
print(concatenarpar)
print(concatenarimpar)

