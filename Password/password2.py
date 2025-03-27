#Password 2

print("INSTRUCCIONES")
print("Introduce una contraseña que contenga: 3 números (distinguiendo rangos), 3 letras (distinguiendo mayúsculas o minúsculas), 2 símbolos")

password=input("Introduce por teclado el password: ")
cont_num=0
cont_let=0
cont_minus=0
cont_mayus=0
cont_sim=0

if len(password)>5 or len(password)<5:
    print("La contrasdeña ha de tener 5 caracteres")
    
else:
    minuscula=False
    for minuscula in password:
        if minuscula.islower()==True:
            minuscula=True
            cont_let+=1
            cont_minus+=1
        elif minuscula.islower()==False:
            cont_let+=1
            cont_mayus+=1
            
    if cont_let>3 or cont_mayus==0 or cont_minus==0:
        print("La contraseña debe tener tres letras, de las cuales algunas sean minúsculas y otras mayúsculas")
        
    numero=False
    for numero in password:
        if password.index("7")
        if numero.isdigit()==True:
            numero=True
            cont_num+=1
            
