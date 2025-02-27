#37. Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado 
#o suspendido.

var1=int(input("Dime el número de notas que deseas introducir: "))

for i in range(var1):
    var2=int(input("Introduce la nota: "))
    if var2>=5:
        print("aprobado")
    else:
        print("suspenso")
