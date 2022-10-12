n=int(input())
L=list(map(int,input().split()))
es=0
os=0
for i in range(n):
    if i%2==0:
        es=es+L[i]
    else:
        os=os+L[i]
print(abs(es-os))