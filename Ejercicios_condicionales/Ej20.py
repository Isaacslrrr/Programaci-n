var1=float(input("Introduce un valor :"))
var2=float(input("Introduce un valor :"))

if 10>var1>0 and 10>var2>0:
    if var1>var2:
        print(var1, "es mayor a", var2)
    elif var1==var2:
        print(var1, "es igual a", var2)
    else:
        print(var2, "es mayor a", var1)
else:
    print("El numero esta fuera de los limites")
    

