# 44. Realiza un programa que recorra todos los números comprendidos de 0 a 100 realizando saltos 
#de 3 en 3. El resultado debe aparecer por pantalla en una línea con los números separados por ‘,’

inicio=0
fin=98
var2=3
print("0")

contador=0
for numero in range(inicio, fin+1):
    if numero % 3==0:
        contador+=var2
        print(contador)