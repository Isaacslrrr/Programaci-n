#23. Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un 
#notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota 
#introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.

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
        
if 10<var1:
    print("La nota que has introducido no esta entre 0 y 10")
    
if var1<0:
    print("La nota que has introducido no esta entre 0 y 10")