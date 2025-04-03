import math

var1=float(input())
minimo=math.floor(var1)
maximo=math.ceil(var1)

if var1%1==0.5:
    redondeo=math.ceil(var1)
else:
    redondeo=round(var1)

print(minimo,maximo,redondeo)