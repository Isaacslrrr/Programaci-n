#27. Mejora el programa anterior para controlar que el valor introducido es una letra y en 
#caso de introducir un nœmero, aparezca un aviso por pantalla

var1=input("Introduce por teclado una letra: ")

if var1.isupper()==True:
    print("La letra es mayuscula")
    
if var1.islower()==True:
    print("La letra es mayuscula")
    
if var1.isnumeric()==True:
    print("Has introducido un número")
    