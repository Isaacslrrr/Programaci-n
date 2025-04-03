lista=[]
var1=input()
lista.append(var1)
if len(var1)>1:
    var2=var1.split()
    listanum=[int(x) for x in var2]
    var3=sum(listanum)
    print(var3)
    
else:
    var2=input()
    lista.append(var2)
    listanum=[int(x) for x in lista]
    var3=sum(listanum)
    print(var3)