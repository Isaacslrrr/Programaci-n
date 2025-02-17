#55. Última vez que reutilizamos el mismo código.. lo prometo . A partir del programa anterior 
#haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y 
#cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While

num1=int(input("Introduce el primer número entero: " ))
5
num2=int(input("Introduce el segundo número entero: " ))
cont_sumas=1


sum_total=num1+num2
print("La suma de estos números es:", sum_total, "y llevas", cont_sumas, "operación realizada.")


while sum_total%2==0 or sum_total<50 : 
    num1=int(input("Introduce el primer número entero: " ))
    num2=int(input("Introduce el segundo número entero: " ))
    cont_sumas+=1
    sum_total+=num1+num2
    print("El acumulado de estos números es:", sum_total, "y llevas", cont_sumas, "operaciones realizadas.")
    
    
else:
    print("ok")
        
    
print("El numero total de las sumas hechas es", cont_sumas)