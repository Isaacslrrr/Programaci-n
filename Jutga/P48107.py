var1=input()
var2=var1.split()
a,b=int(var2[0]),int(var2[1])

if b>0:
    divis=a//b
    resto=a%b
    print(divis, resto)


