#31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. 
#Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su 
#índice.

sentence="A quién madruga Dios ayuda"

var1=input("Introduce un valor :")

if var1 in sentence:
    varindex=sentence.find(var1)
    print("La palabra está en la frase y está en el índice", varindex)

else:
    print("La palabra no está en la frase")