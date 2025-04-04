#38. A partir del programa anterior, establece los rangos para que el usuario no pueda introducir 
#notas inferiores a 0 y superiores a 10

var1=int(input("Dime el número de notas que deseas introducir: "))
var2=0
for i in range(var1):
    if var2>=0 and var2<=10:
        var2=int(input("Introduce la nota: "))
        if var2>=5 and var2<=10:
            print("aprobado")
        elif var2<5 and var2>=0:
            print("suspenso")
    else:
        print("no está entre el rango permitido")
         