#60. Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. 
#Utiliza únicamente el while

multiplicador=int(input("Introduce un número para printear por pantalla su tabla de multiplicación: "))

columna=1
total=0

while multiplicador<=10 and columna<=10:
    total=multiplicador*columna
    print(multiplicador, "x", columna, "=", total)
    columna+=1
    
if multiplicador>10:
    print("El valor introducido es mayor a 10." )