#71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en
#esta lista no deben almacenarse las letras que se han introducido repetidas.

lista=[]

var1=input("introduce una letra: " )
var2=input("¿Deseas repetir s/n: ")
lista.append(var1)
while var2=="s":
    var1=input("introduce una letra: " )
    lista.append(var1)
    var2=input("¿Deseas repetir s/n: ")
    
var3=list(set(lista))

print(var3)