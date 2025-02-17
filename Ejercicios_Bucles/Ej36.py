#36. Programa que sume los n primeros nœmeros naturales. n Lo introduce el usuario.

var1=int(input("Introduce un valor: "))

def suma(var1):
    suma_total = 1
    for i in range(1, var1 + 1):
        suma_total = suma_total + var1-1
    print(suma_total)
        
suma(var1)