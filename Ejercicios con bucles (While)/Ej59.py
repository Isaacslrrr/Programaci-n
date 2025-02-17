#59. Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que 
#intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o 
#menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe 
#mostrarse por pantalla un mensaje y el número de intentos.

import random

cont_veces=0

num=int(input("Introduce el número secreto: "))
numero_secreto=random.randint(0, 1000)

if num==numero_secreto:
    print("Has adivinado el número secreto")

else:
    while num!=numero_secreto:
        if num>numero_secreto:
            print("El número introducido es mayor al secreto")
        if num<numero_secreto:
            print("El número introducido es menor al secreto")
        cont_veces+=1
        
        num=int(input("Introduce el número secreto: "))
            
    
print("El número de intentos ha sido:", cont_veces)