
numeros=input("Introduce los números separados")

lsitanum1=[]

listanum1=numeros.split()

print(listanum1)

lista3=set(listanum1)

print(lista3)

lista2=[int(x) for x in listanum1]

total=sum(lista2)

print(total)