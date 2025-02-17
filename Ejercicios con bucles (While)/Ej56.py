#56. Realiza un programa que gestione un establecimiento de venta de bocadillos. Un pedido se 
#compone de: bocadillo, acompañamiento y bebida. Un cliente puede pedir más de un pedido. El 
#dependiente a partir del menú (ver imagen), se encarga de introducir los datos. El menú solo se 
#visualiza una vez al ejecutar el programa. El programa debe preguntar al dependiente tras la 
#realización de un pedido, si quiere gestionar otro. 
#El establecimiento contempla los siguientes descuentos:
#Si el total a pagar es entre 20 y 30 euros, se aplica un descuento del 5%
#Si el total a pagar es superior a 30 euros, se aplica un descuento del 15%
#Una vez se finaliza la introducción de todos los pedidos de un cliente, debe aparecer por pantalla:
#• El número de pedidos realizados
#• Total a pagar.
#• Total con IVA (10%)
#• Total con el descuento aplicado.

print("MENÚ")
print("1. Bocadillo de calamares- 9 €")
print("2. Bocadillo de chistorra - 4.5 €")
print("3. Bikini de jamón - 2.5 €")
print("ACOMPAÑAMIENTO")
print("1. Patatas finas - 1.5 €")
print("2. Patatas gruesas - 1.75 €")
print("3. Patatas rústicas - 2 €")
print("BEBIDAS")
print("1. Coca cola - 2 €")
print("2. Acuarius - 1.5 €")
print("3. Agua - 1 €")


pedidos=0
total=0
conIVA=0
total_final=0
menú=0
pedir=0

continuar=input("Quieres pedir algo (si/no): ")
if continuar=="si":

    menú=int(input("Que desea del menú: "))
    
    if menú==1:
        total+=9
    if menú==2:
        toal+=4.5
    if menú==3:
        total+=2.5
        
    acompañamiento=int(input("Que desea del acompañamiento: "))
    
    if menú==1:
        total+=1.5
    if menú==2:
        toal+=1.75
    if menú==3:
        total+=2
        
    bebidas=int(input("Que desea de beber: "))
    
    if menú==1:
        total+=2
    if menú==2:
        toal+=1.5
    if menú==3:
        total+=1
        
    pedidos+=1  
      
    pedir=input("Quieres hacer otro pedido (si/no): ")

    while pedir=="si":
        menú=int(input("Que desea del menú: "))
        
        if menú==1:
            total+=9
        if menú==2:
            toal+=4.5
        if menú==3:
            total+=2.5
            
        acompañamiento=int(input("Que desea del acompañamiento: "))
        
        if menú==1:
            total+=1.5
        if menú==2:
            toal+=1.75
        if menú==3:
            total+=2
            
        bebidas=int(input("Que desea de beber: "))
        
        if menú==1:
            total+=2
        if menú==2:
            total+=1.5
        if menú==3:
            total+=1
            
        pedidos+=1
        pedir=input("Quieres hacer otro pedido (si/no): ")
    
    else:
        conIVA=10*total/100
        total_final=total+conIVA
        print("El total de pedidos realizados es:", pedidos)
        print("El total a pagar es:", total)
        print("El total a pagar +IVA es:", total_final)
        
        if total>19 and total<31:
            total_final=total_final-(5*total_final/100)
            print("Lo que has de pagar con el DESCUENTO de 5% es:", total_final)
            
        if total>30:
            total_final=total_final-(15*total_final/100)
            print("Lo que has de pagar con el DESCUENTO de 15% es:", total_final)
            
        else:
            print("¡Muchas gracias!")
    
if continuar=="no":
    print("ok")