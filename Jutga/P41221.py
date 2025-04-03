lista=[]
while len(lista)<3:
    var1=input()
    var4=var1.split()
    for num in var4:
        if len(lista)<3:
            lista.append(int(num))

var3=sum(lista)
print(var3)
