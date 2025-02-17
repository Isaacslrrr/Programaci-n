milista=[]
total=0
listamulti=[]

numero=int(input("Introduce un número: "))

while numero!=0:
    milista.append(numero)
    numero=int(input("Introduce otro número o 0 para acabar: "))
    
print(max(milista))
print(min(milista))

for recorrer in milista:
    multi=recorrer*2
    listamulti.append(multi)
    
print("Lista multiplicada", listamulti)