# 47. Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe 
#mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b 
#la secuencia en descenso. Respeta el formato de salida

a=int(input("Introduce el primer intervalo: "))
b=int(input("Introduce el segundo intervalo: "))

if a<b:
    rango=range(a, b+1)
else:
    rango=range(a, b-1,-1)

resultado='-'.join(map(str, rango))

print(resultado)
