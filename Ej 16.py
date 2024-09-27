#16. Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El 
#resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un 
#resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso
#(raíz y división).

var1=float(input("Introduce un valor :"))

import math

var2=(math.sqrt(var1))
var3=var2//2

print("La raíz es", var2)
print("La división es", var3)
