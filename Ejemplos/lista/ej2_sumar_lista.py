milista=[]
total=0

numero=int(input("Introduce un número: "))

while numero!=0:
    milista.append(numero)
    numero=int(input("Introduce otro número o 0 para acabar: "))
    
print(max(milista))
print(min(milista))

for recorrer in range(0, len(milista)):
    total=total+milista[recorrer]
    
print(total)