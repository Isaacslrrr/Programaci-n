lista1=[]

lista2=[]

lista3=[]

valores=input("Introduce los valores separados por un guion: ")
lista1=valores.split("-")

for recorrer in lista1:
    if recorrer.isnumeric():
        lista2.append(recorrer)
    else:
        lista3.append(recorrer)
        
print(lista1)
print(lista2)
print(lista3)
