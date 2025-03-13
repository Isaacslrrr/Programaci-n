import random

seguir = 'si'
while seguir=='si':
    puntos=0
    print("\nNueva partida!")
    otra='si'
    while otra=='si':
        carta=random.randint(1, 12)
        while carta in [8, 9]:
            carta=random.randint(1, 12)
        valor=carta if carta < 10 else 0.5
        puntos+=valor
        print(f"Carta: {carta}, Puntos: {puntos}")
        
        if puntos>7.5:
            print("Has perdido la partida!")
            otra='no'
        elif puntos==7.5:
            print("Enhorabuena, has ganado la partida!")
            otra='no'
        else:
            otra=input("¿Otra carta? (si/no): ")
    
    if puntos>=6 and puntos<=7:
        print("Has sido un poco conservador")
    if puntos<=5.9:
        print("Quizás tendrías que arriesgar un poco ¿no?")
    
    seguir=input("¿Jugar de nuevo? (si/no): ")
