
print("INSTRUCCIONES")
print("1.-La longitud de la contraseña tiene que tener entre 6 y 8 caracteres")
print("2.-Forzar los siguuientes valores según la posición indicada")
print("Posición 1: Un número mayor o igual a 1 i menor o igual a 5.")
print("Posición 2: Una letra en minúscula.")
print("Posición 3: Una letra en mayúscula.")
print("Posición 4: Uno de los siguinetes símbolos *, _, @")
print("Posición 5: Una letra minúscula.")
print("Posición 6: Un número mayor o igual a 6 i menor o igual a 9.")
print("Posición 7: Uno de los siguinetes símbolos &, /, #")
print("Posición 8: Un número menor o igual que 5.")


password=input("Introduce por teclado el password: ")

#Si la contraseña es mayor a 8 o menor a 6 la contraseña saldrá incorrecta, lo he hecho con el len y el or
if len(password)>9 or len(password)<5:
    print("Contraseña muy corta, debe tener entre 6-8 caracteres")
#Si la contraseña es menor a 7 y mayor a 5 que haga todos los requisitos pero solo para 6 valores#
if len(password)<7 and len(password)>5:
    pos1=password[0]
    if pos1>str(6) and pos1<str(0):
        print("Contraseña incorrecta, posición 1 no está entre 1-5")
    pos2=password[1]
    if pos2.islower()==False:
        print("Contraseña incorrecta, posición 2 minúscula")
    pos3=password[2]
    if pos3.isupper()==False:
        print("Contraseña incorrecta, posición 3 mayúscula")
    pos4=password[3]
    if pos4!="*" and pos4!="_" and pos4!="@":
        print("Contraseña incorrecta, posición 4 debe ser *, _, @")
    pos5=password[4]
    if pos5.islower()==False:
        print("Contraseña incorrecta, posición 5 minúscula")
    pos6=password[5]
    if pos6>str(10) and pos6<str(5):
        print("Contraseña incorrecta, posición 6 no está entre 6-9")
    else:
        print("Felicidades, contraseña correcta.")

#Si la contraseña es menor a 8 y mayor a 6 que haga todos los requisitos pero para 7 valores#            
if len(password)<8 and len(password)>6: 
    pos7=password[6]
    if pos7!="&" and pos7!="/" and pos7!="#":
        print("Contraseña incorrecta, posición 7 debe ser , _, @")
    else:
        print("Felicidades, contraseña correcta")
#Si la contraseña es menor a 9 y mayor a 7 que haga todos los requisitos para 8 valores#          
if len(password)<9 and len(password)>7: 
    pos8=password[7]
    if pos8>str(6):
        print("Contraseña incorrecta, posición 9 es mayor a 5")
    else:
        print("Felicidades, contraseña correcta")
    
        
       
            
    