a1,b1,a2,b2=map(int,input().split())

if b1 < a2 or b2 < a1:
    print("[]")
else:
    x =max(a1, a2)
    y =min(b1, b2)
    print(f"[{x},{y}]")