n=int(input())
L=list(map(int,input().split()))
s=0
for i in range(n):
    if i%2!=0:
        s=s+L[i]
print(s)