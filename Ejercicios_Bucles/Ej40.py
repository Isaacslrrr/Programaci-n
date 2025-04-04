#40. Crea un programa que cuente todos los números pares hasta el número 50

inicio=1
fin=50

contador_pares=0
for numero in range(inicio, fin+1):
    if numero % 2==0:
        contador_pares+=1

print(f"Hay {contador_pares} números pares entre {inicio} y {fin}.")
print((f"Hay {contador_pares} números impares entre {inicio} y {fin}."))
