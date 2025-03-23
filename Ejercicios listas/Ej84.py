#84. A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las
#palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la
#palabra secreta. El usuario tendrá 3 oportunidades para adivinar la palabra. 
import random
lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]

contador=3
var1=random.choice(lista)
palabra=list(var1)
random.shuffle(palabra)

print(palabra)
var2=0

while contador<=3 and var2!=var1:
    var2=input("Introduce la palabra ordenada: ")
    if var2==var1:
        print("genial")
        
    elif var2!=var1:
        print("mal")
        contador-=1


    