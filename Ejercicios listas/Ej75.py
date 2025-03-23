#75. Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por
#pantalla los siguientes resultados:
#a. Cantidad total de valores
#b. Cantidad de números
#c. Cantidad de letras
#d. Cantidad de mayúsculas
#e. Suma de los valores numéricos

lista=["a","b","D","x","r","X",3,"h","w",2,"i"]
numeros=[]
letras=[]
letrasmay=[]
letrasmin=[]
var1=len(lista)
print(var1)

for i in lista:
    if isinstance(i, (int, float)):
        numeros.append(i)
    elif isinstance(i, str):
        letras.append(i)
        if i.islower():
            letrasmin.append(i)
        if i.isupper():
            letrasmay.append(i)
        
print(letras, "letras")
print(numeros, "numeros")
print(letrasmin, "letras minusculas")
print(letrasmay, "letras mayusculas")
print(sum(numeros), "la suma")
