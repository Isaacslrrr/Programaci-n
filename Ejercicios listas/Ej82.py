#82. Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al
#azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine
#la palabra

import random
lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
var1=random.choice(lista)
var2=0

while var2!=var1:
    var2=input("Introduce la palabra: ")
    if var1==var2:
        print("Correcto")
    else:
        print("incorrecto")
