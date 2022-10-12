m=int(input())
def fc(n):
    fc=0
    for i in range(1,n):
        if n%i==0:
            fc=fc+i
    return fc
if m==fc(m):
    print("True")
else:
    print("False")