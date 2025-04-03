a1,b1,a2,b2=map(int,input().split())

inicio_inter=max(a1,a2)
fin_inter=min(b1,b2)

if a1==a2 and b1==b2:
    print(f"= , [{inicio_inter},{fin_inter}]")
elif a1>=a2 and b1<=b2:
    print(f"1 , [{inicio_inter},{fin_inter}]")
elif a2>=a1 and b2<=b1:
    print(f"2 , [{inicio_inter},{fin_inter}]")
else:
    if inicio_inter <= fin_inter:
        print(f"? , [{inicio_inter},{fin_inter}]")
    else:
        print(f"? , []")