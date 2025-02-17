#53. A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las 
#sumas y el número de repeticiones. Con While

num1=int(input("Introduce el primer número entero: " ))
num2=int(input("Introduce el segundo número entero: " ))
cont_sumas=1

sum_total=num1+num2
print("La suma de estos números es:", sum_total)

continuar=input("Quieres repetir la operación (si/no): " )

while continuar=="si": 
    num1=int(input("Introduce el primer número entero: " ))
    num2=int(input("Introduce el segundo número entero: " ))
    cont_sumas+=1
    sum_total=num1+num2
    print("La suma de estos números es:", sum_total)
    
    continuar=input("Quieres repetir la operación (si/no): ")
    
else:
    print("ok")
    
    
print("El numero total de las sumas hechas es", cont_sumas)