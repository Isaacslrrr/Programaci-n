#51. A partir del programa anterior, modifica el código para que sea el usuario quién introduzca el 
#número de veces que desea que repita la frase Buenos días. Con While

var1=int(input("Introduce el número de veces que quieres que se imprima por pantalla 'Buenos días':" ))
               
palabra=1
num_max=var1+1

while palabra<num_max:
    print("Buenos dias")
    palabra+=1