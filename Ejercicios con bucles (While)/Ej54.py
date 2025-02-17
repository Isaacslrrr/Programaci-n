#54. Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total 
#de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta 
#preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la 
#operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el 
#mensaje del acumulado es singular o plural.. . Con While

num1=int(input("Introduce el primer número entero: " ))
5
num2=int(input("Introduce el segundo número entero: " ))
cont_sumas=1


sum_total=num1+num2
print("La suma de estos números es:", sum_total, "y llevas", cont_sumas, "operación realizada.")


while cont_sumas<51: 
    num1=int(input("Introduce el primer número entero: " ))
    num2=int(input("Introduce el segundo número entero: " ))
    cont_sumas+=1
    sum_total+=num1+num2
    print("El acumulado de estos números es:", sum_total, "y llevas", cont_sumas, "operaciones realizadas.")
    
    
if cont_sumas==51:
    continuar=input("Quieres repetir la operación (si/no): ")
    while continuar=="si": 
        num1=int(input("Introduce el primer número entero: " ))
        num2=int(input("Introduce el segundo número entero: " ))
        cont_sumas+=1
        sum_total=num1+num2
        print("La suma de estos números es:", sum_total, "y llevas", cont_sumas, "operaciones realizadas.")
        continuar=input("Quieres repetir la operación (si/no): ")

    else:
        print("ok")
        
    
print("El numero total de las sumas hechas es", cont_sumas)