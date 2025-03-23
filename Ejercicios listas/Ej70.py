#70. Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez
#introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por
#pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el
#formato de entrada y salida tal y como se muestra en el testeo.

lista1=[]
lista2=[]

var1=int(input("introduce la cantidad de palabras: "))
for i in range(var1):
    var2=input("introduce la palabra: ")
    lista1.append(var2)
    lista2.append(var2)

lista2.reverse()
print(lista1)
print(lista2)
