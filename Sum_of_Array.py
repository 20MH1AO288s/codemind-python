n=int(input())
L=list(map(int,input().split()))
s=0
for i in range(n):
    s+=L[i]
print(s)