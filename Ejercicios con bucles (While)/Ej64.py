#64. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor 
#-99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas:
#a) total de pares
#b) total de impares
#c) total de números positivos
#d) total de números negativos
#e) total de ceros
#f) total de la suma de todos los números introducidos

var1=int(input("Introduce un número: "))

cont_par=0
cont_impar=0
cont_pos=0
cont_neg=0
cont_0=0
suma=0

if var1%2==0:
    cont_par+=1
else:
    cont_impar+=1
    
if var1>0:
    cont_pos+=1
elif var1==0:
    cont_0+=1
else:
    cont_neg+=1
    
suma+=var1

while var1>-99 and var1!=-99:
    var1=int(input("Introduce un número: "))
    
    if var1%2==0:
        cont_par+=1
    else:
        cont_impar+=1
        
    if var1>0:
        cont_pos+=1
    elif var1==0:
        cont_0+=1
    else:
        cont_neg+=1
        
    suma+=var1
    
print("La cantidad de números pares es", cont_par)
print("La cantidad de números impares es", cont_impar)
print("La cantidad de números positivos es", cont_pos)
print("La cantidad de números negativos es", cont_neg)
print("La cantidad de zeros es", cont_0)
print("La suma total es", suma)