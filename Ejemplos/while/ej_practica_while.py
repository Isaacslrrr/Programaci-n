#Contar todos los pares entre 1-20 con while

contador=1
contador_pares=0

while contador<=20:
    if contador%2==0:
        contador_pares+=1
    contador+=1
    
print("El total de pares es", contador_pares)