frase=input("Introduce una frase: ")

milista=frase.split(",")

print(milista[2])

palabra=input("Introduce la palabra que quieres contar: ")

print(milista.count(palabra))