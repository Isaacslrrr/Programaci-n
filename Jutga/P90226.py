var1=input()
var2=var1.split()


longitud=len(var2)
if var2[1]>var2[0]:
    print(var2[0], "<", var2[1])
elif var2[1]<var2[0]:
    print(var2[0], ">", var2[1])
elif var2[1]==var2[0]:
    print(var2[0], "=", var2[1])
    
    