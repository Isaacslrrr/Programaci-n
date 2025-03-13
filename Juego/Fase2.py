import random

deposito=100
seguir='si'
while seguir=='si' and deposito>0:
    puntos=0
    print(f"\nNueva partida! Depósito actual: {deposito} puntos")
    otra='si'
    while otra=='si':
        carta=random.randint(1,12)
        while carta in [8,9]:
            carta=random.randint(1,12)
        valor=carta if carta<10 else 0.5
        puntos+=valor
        print(f"Carta: {carta}, Puntos: {puntos}")
        
        if puntos>7.5:
            print("Has perdido la partida!")
            deposito-=10
            otra='no'
        elif puntos==7.5:
            print("Enhorabuena, has ganado la partida!")
            deposito += 10
            otra='no'
        else:
            otra=input("¿Otra carta? (si/no): ")
    
    if puntos<7.5:
        if puntos>=6:
            print("Has sido un poco conservador")
            deposito+=5
        else:
            print("Quizás tendrías que arriesgar un poco ¿no?")
            deposito-=5
    
    if deposito<=0:
        print("Te has quedado sin puntos. Fin del juego.")
        break
    
    seguir = input("¿Jugar de nuevo? (si/no): ")
    
print("Tu deposito es de", deposito)
