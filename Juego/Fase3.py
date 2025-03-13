import random

seguir = 'si'
while seguir=='si':
    puntos=0
    print("\nNueva partida!")
    otra=input("Te doy una carta? si/no: ")
    while otra=='si':
        carta=random.randint(1, 12)
        while carta in [8, 9]:
            carta=random.randint(1, 12)
        valor=carta if carta < 10 else 0.5
        puntos+=valor
        print(f"Carta: {carta}, Puntos: {puntos}")
       
        if puntos>7.5:
            print("Muy bien, ahora es el turno de la banca")
            otra='no'
        else:
            print("Ahora es el turno de la banca")
            puntos2=0
            if puntos<7.5:
                while puntos2<=4.5:
                    carta=random.randint(1, 12)
                    while carta in [8, 9]:
                        carta=random.randint(1, 12)
                    valor=carta if carta < 10 else 0.5
                    puntos2+=valor
                    print("La banca tiene la"f"Carta: {carta}, Puntos: {puntos}", )
                if puntos2>=5 and puntos2<=7.5:
                    print("La banca se planta con", puntos2, "puntos")
                    
if puntos2<puntos:
    print("Has ganado con", puntos, "puntos")
elif puntos2>puntos:
    print("Ha ganado la banca con", puntos2, "puntos")