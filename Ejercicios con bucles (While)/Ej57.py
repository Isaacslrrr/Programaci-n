#57. Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa 
#debe controlar si el usuario introduce un número no comprendido entre 1 y 5

import random
num=int(input("Introduce el número secreto: "))
numero_secreto=random.randint(1, 5)

if num>5:
    print("El número es mayor a 5")
    
else:
    while num!=numero_secreto:
        print("no es el numero, recuerda que el número no puede ser mayor a 5")
        num=int(input("Vuelve a intentarlo: "))
    else:
        print("very good")
       
