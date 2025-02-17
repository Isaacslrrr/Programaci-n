#58. Modifica el programa anterior para que tengas 3 intentos. Utiliza while

import random

cont_veces=0

num=int(input("Introduce el número secreto: "))
numero_secreto=random.randint(1, 5)


if num>5:
    print("El número es mayor a 5")
    
else:
    while num!=numero_secreto and cont_veces<2:
        cont_veces+=1
        print("no es el número")
        num=int(input("Vuelve a intentarlo: "))
    
    print("Has alcanzado el máximo de intentos.")
        
    if num==numero_secreto:
        print("very good")

   