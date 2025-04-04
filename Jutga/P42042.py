var1=input()

if var1=="a" or var1=="e" or var1=="i" or var1=="o" or var1=="u" or var1=="A" or var1=="E" or var1=="I" or var1=="O" or var1=="U":
    if var1.isupper() and len(var1)==1:
        print("majuscula")
        print("vocal")
    elif var1.islower() and len(var1)==1:
        print("minuscula")
        print("vocal")
else:
    if var1.isupper() and len(var1)==1:
        print("majuscula")
        print("consonant")
    elif var1.islower() and len(var1)==1:
        print("minuscula")
        print("consonant")