num1=[]
num2=[]
num3=[]

valores=input()
num1, num2, num3 = map(int, valores.split())
maximo=max(num1, num2, num3)
print(maximo)
