n=int(input())
m=int(input())
c=0
s=0
for i in range(1,n):
    if n%i==0:
        c+=i
for j in range(1,m):
    if m%j==0:
        s+=j
if s==n and c==m:
    print("Amicable")
else:
    print("Not Amicable")