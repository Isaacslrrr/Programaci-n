#32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para 
#no distinguir entre mayúsculas y minúsculas

sentence="A quién madruga Dios ayuda"
var1=input("Introduce un valor :")

sentence_2=sentence.lower()
var2=var1.lower()

if var2 in sentence_2:
    varindex=sentence_2.find(var2)
    print("La palabra está en la frase y está en el índice", varindex)

else:
    print("La palabra no está en la frase")