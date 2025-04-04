#45. Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string
#distinguiendo vocales y las consonantes

palabra=input("Introduce una palabra: ")
var1=[]
var2=[]

vocales="aeiouAEIOU"

for letra in palabra:
    if letra in vocales:
        print(letra, " es una vocal.")
    else:
        print(letra, "es una consonante.")
