#72. A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y
#no deben almacenarse en la lista

letras = []
ingresadas = set()

repetir = "s"
while repetir == "s":
    letra = input("Introduce una letra: ").strip().lower()
    
    if letra in ["á", "à", "â", "ä"]:
        letra = "a"
    elif letra in ["é", "è", "ê", "ë"]:
        letra = "e"
    elif letra in ["í", "ì", "î", "ï"]:
        letra = "i"
    elif letra in ["ó", "ò", "ô", "ö"]:
        letra = "o"
    elif letra in ["ú", "ù", "û", "ü"]:
        letra = "u"
    
    if len(letra) == 1 and letra.isalpha() and letra not in ingresadas:
        ingresadas.add(letra)
        letras.append(letra)
    
    repetir = input("¿Deseas repetir s/n: ").strip().lower()

print(letras)
