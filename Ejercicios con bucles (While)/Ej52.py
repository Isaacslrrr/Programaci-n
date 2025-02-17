#52. Realiza un programa que sume dos números enteros por teclado y presente el resultado por 
#pantalla. El programa preguntará si deseas o no repetir la operación. Con While


num1=int(input("Introduce el primer número entero: " ))
num2=int(input("Introduce el segundo número entero: " ))

sum_total=num1+num2
print("La suma de estos números es:", sum_total)

continuar=input("Quieres repetir la operación (si/no): " )

while continuar=="si": 
    num1=int(input("Introduce el primer número entero: " ))
    num2=int(input("Introduce el segundo número entero: " ))
    
    sum_total=num1+num2
    print("La suma de estos números es:", sum_total)
    
    continuar=input("Quieres repetir la operación (si/no): ")
    
else:
    print("ok")