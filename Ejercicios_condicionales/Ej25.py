#25. Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.

var1=float(input("Introduce tu nota :"))

if 11>var1>-1:
    if 6.5>=var1>=5:
        print("Has sacado un", var1, ",un satisfactorio")
    elif 8.5>var1>6.5:
        print("Has sacado un", var1, ",un notable")
    elif 10>=var1>=8.5:
         print("Has sacado un", var1, ",un excelente")
    else:
        print("Has sacado un", var1, ",has suspendido")
        
if 10<var1 or var1<0:
    print("La nota que has introducido no esta entre 0 y 10")

