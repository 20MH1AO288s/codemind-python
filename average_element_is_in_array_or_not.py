n=int(input())
L=list(map(int,input().split()))
avg=sum(L)//n
if avg in L:
    print(True)
else:
    print(False)