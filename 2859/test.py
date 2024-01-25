a = 5
ans = 0
while a!=0:
    if a & 1 == 1:
        ans+=1 
    a = a >>1
print(ans)