import random

cartas=[1,2,3,4,5,6,7,10,11,12]

carta=random.choice(cartas)
alias=input("Introduce tu alias: ")
seguir = 'si'
while seguir=='si':
    puntos=0
    print("\nNueva partida!")
    otra='si'
    while otra=='si':
        carta=random.choice(cartas)
        valor=carta if carta < 10 else 0.5
        puntos+=valor
        print(alias, "tienes la "f"carta: {carta}, Puntos: {puntos}")  
        if puntos>7.5:
            print("Ahora le tocará a la banca!")
            otra='no'
        elif puntos==7.5:
            print("Enhorabuena", alias,"has conseguido el siete y medio!")
            otra='no'
            
        else:
            otra=input("¿Otra carta? (si/no): ")
    

    
    seguir=input("Comienza... (press enter) ")
    print("LA BANCA")
    puntos2=0
    while puntos2<=4.5:
        carta=random.choice(cartas)
        valor1=carta if carta < 10 else 0.5
        puntos2+=valor1
        print("La banca tiene la "f"cartas: {carta}, Puntos: {puntos2}", )
        input()
    if puntos2>=5 and puntos2<=7.5:
        print("La banca se planta con", puntos2, "puntos")


if puntos>puntos2 and puntos<=7.5:
    print(alias, "has ganado con", puntos, "puntos.")

elif puntos>7.5 and puntos2<=7.5:
    print("Ha ganado la banca con", puntos2, "puntos.")    

elif puntos2>7.5 and puntos<=7.5:
    print(alias, "has ganado con", puntos, "puntos.")    
    
elif puntos2>puntos and puntos2<=7.5:
    print("Ha ganado a la banca con", puntos2, "puntos.")
    
elif puntos>7.5 and puntos2>7.5:
    print("¡Tanto la banca como tu habeis perdido!")
    
elif puntos==puntos2 and puntos<=7.5 and puntos2<=7.5:
    print("Tanto la banca como tú teneis los mismos puntos, ¡Empate!")
    
var5=input("Quieres jugar otra partida? (si/no): ")
while var5=="si":
    cartas=[1,2,3,4,5,6,7,10,11,12]

    carta=random.choice(cartas)
    alias=input("Introduce tu alias: ")
    seguir = 'si'
    while seguir=='si':
        puntos=0
        print("\nNueva partida!")
        otra='si'
        while otra=='si':
            carta=random.choice(cartas)
            valor=carta if carta < 10 else 0.5
            puntos+=valor
            print(alias, "tienes la "f"carta: {carta}, Puntos: {puntos}")  
            if puntos>7.5:
                print("Ahora le tocará a la banca!")
                otra='no'
            elif puntos==7.5:
                print("Enhorabuena", alias,"has conseguido el siete y medio!")
                otra='no'
                
            else:
                otra=input("¿Otra carta? (si/no): ")
        

        
        seguir=input("Comienza... (press enter) ")
        print("LA BANCA")
        puntos2=0
        while puntos2<=4.5:
            carta=random.choice(cartas)
            valor1=carta if carta < 10 else 0.5
            puntos2+=valor1
            print("La banca tiene la "f"cartas: {carta}, Puntos: {puntos2}", )
            input()
        if puntos2>=5 and puntos2<=7.5:
            print("La banca se planta con", puntos2, "puntos")


    if puntos>puntos2 and puntos<=7.5:
        print(alias, "has ganado con", puntos, "puntos.")

    elif puntos>7.5 and puntos2<=7.5:
        print("Ha ganado la banca con", puntos2, "puntos.")    

    elif puntos2>7.5 and puntos<=7.5:
        print(alias, "has ganado con", puntos, "puntos.")    
        
    elif puntos2>puntos and puntos2<=7.5:
        print("Ha ganado a la banca con", puntos2, "puntos.")
        
    elif puntos>7.5 and puntos2>7.5:
        print("¡Tanto la banca como tu habeis perdido!")
        
    var5=input("Quieres jugar otra partida? (si/no): ")
if var5=="no":
    print("Ok!")