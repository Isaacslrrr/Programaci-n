#22. Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. 
#Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.

var1=float(input("Introduce tu nota :"))

if 11>var1>-1:
    if var1>=5:
        print("Has sacado un", var1, "y has aprobado")
    elif var1<5:
        print("Has sacado un", var1, "y has suspendido")   
        
if 10<var1 or var1<0:
    print("La nota que has introducido no esta entre 0 y 10")