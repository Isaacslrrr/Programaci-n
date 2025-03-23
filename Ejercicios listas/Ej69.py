#69. Realiza un programa que permita introducir una cantidad exacta de números, cada número se
#irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números
#ordenados de menor a mayor.

lista=[]

var1=int(input("Valores que deseas introducir: "))
for i in range(var1):
     var2=input("Introduce el valor: ")
     lista.append(var2)
     
print(lista)



