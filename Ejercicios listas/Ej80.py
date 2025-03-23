#80. Utilizando listas, crea un programa que te permita determinar si un número es decimal o no. 

var1=input("quieres introducir algun valor? si/no:  ")
decimal=[]
entero=[]

if var1=="si":
    while var1=="si":
        var2=float(input("introduce un valor: "))
        if var2.is_integer():
            entero.append(var2)
            print("no es decimal")
        else:
            decimal.append(var2)
            print("es decimal")
        var1=input("quieres introducir algun valor? si/no:  ") 
        
        