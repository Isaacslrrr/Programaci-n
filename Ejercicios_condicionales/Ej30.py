#30. Realiza un programa que controle si la longitud de una frase introducida por teclado es
#igual, menor o mayor de 11 caracteres. Utiliza elif

var1=input("Introduce por teclado una frase: ")

letras=len(var1)

if letras==11:
    print("La frase tiene 11 caracteres")
    
elif letras<11:
    print("La frase tiene menos de 11 caracteres")
    
else:
    print("La frase tiene 11 o más caracteres")