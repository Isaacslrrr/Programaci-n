var1=input()
var2=var1.split()
listanum=[int(x) for x in var2]

hora,minuto,segundo=listanum
segundo+=1
if segundo==60:
    segundo=0
    minuto+=1
    if minuto==60:
        minuto=0
        hora=(hora+1)%24

print(f"{hora:02}:{minuto:02}:{segundo:02}")