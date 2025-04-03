anyo=int(input())

if (anyo%4==0 and anyo%100!=0) or (anyo%400==0):
    print("YES")
else:
    print("NO")
    