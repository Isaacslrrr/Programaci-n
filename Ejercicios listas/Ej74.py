#74. A partir del programa anterior, haz que se visualicen tanto las palabras que se repiten o no de
#entre las 2 listas.


lista1 = ["casa", "mesa", "sal", "sol", "agua"]
lista2 = ["casa", "luz", "tres", "tren", "sol", "pan"]

set1=set(lista1)
set2=set(lista2)

rep=set1.intersection(set2)
norep1=set1.difference(set2)
norep2=set2.difference(set1)


print(rep)
print(norep1, norep2)

