#26. Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si 
#está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.


var1=input("Introduce por teclado una letra: ")

if var1.isupper()==True:
    print("La letra es mayúscula")
    
if var1.islower()==True:
    print("La letra es minúscula")
    
else:
    print("La letra es mayúscula ¿?")