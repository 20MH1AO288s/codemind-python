n=int(input())
L=[]
while n>0:
    r=n%10
    L.append(r)
    n=n//10
print(max(L))