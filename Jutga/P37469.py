var1=int(input())

horas=var1//3600
var1%=3600
minutos=var1//60
segundos=var1%60

print(horas, minutos, segundos)
