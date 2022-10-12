n=int(input())
L=list(map(int,input().split()))
s=0
for i in L:
    if i%2==0:
        s=s+i
print(s)