milista=[]
total=0
listamulti=[]

numero=int(input("Introduce un número: "))

while numero!=0:
    milista.append(numero)
    numero=int(input("Introduce otro número o 0 para acabar: "))
    
print(max(milista))
print(min(milista))

listamulti=[x * 2 for x in milista]

print("Lista multiplicada", listamulti)