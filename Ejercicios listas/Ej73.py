#73. Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están
#repetidos o no en la lista2 (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se
#repiten y cuales no

lista1 = ["casa", "mesa", "sal", "sol", "agua"]
lista2 = ["casa", "luz", "tres", "tren", "sol", "pan"]

set1=set(lista1)
set2=set(lista2)

repetidas=set1.intersection(lista2)
norep=set1.difference(lista2)

print("las rep son", repetidas)
print("las no rep son", norep)
