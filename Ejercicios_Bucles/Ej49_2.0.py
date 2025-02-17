#49. A partir del programa anterior, modifica el código para que al introducir la letra por teclado te 
#indique en qué posición de la palabra se encuentra la letra.

posicion=1

var=input("Introduce una palabra: ")
letra=input("Introduce la letra: ")
 
for recorrido in var:
   
    if recorrido==letra:
        print("La letra se encuentra", letra, " es", posicion)
    posicion=posicion+1