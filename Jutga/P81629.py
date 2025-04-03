monedas_y_billetes=[50000,20000,10000,5000,2000,1000,500,200,100,50,20,10,5,2,1]

var1=input()
var2=var1.split()

euros=int(var2[0])
centimos=int(var2[1])

total_centimos=euros*100+centimos

monedas_billetes={}

for valor in monedas_y_billetes:
    cantidad=total_centimos//valor
    if cantidad>0:
        monedas_billetes[valor]=cantidad
    else:
        monedas_billetes[valor]=0
    total_centimos%=valor

for valor in monedas_y_billetes:
    if valor>=100:
        print(f"{valor//100} euros en bits: {monedas_billetes[valor]}")
    else:
        print(f"Monedes de {valor} centims: {monedas_billetes[valor]}")
        