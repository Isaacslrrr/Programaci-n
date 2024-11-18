#28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza 
#elif.


var1=input("Introduce por teclado una letra: ")

if var1.isupper()==True:
    print("La letra es mayúscula")
    
elif var1.islower()==True:
    print("La letra es minúscula")
    
elif var1.isnumeric()==True:
    print("Has introducido un número")
    
else:
    print("Has introducido un simbolo")