num1=[]
num2=[]

valores=input()
num1, num2 = map(int, valores.split())
maximo=max(num1, num2)
print(maximo)
