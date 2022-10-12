n=int(input())
a=len(str(n))
c=n*n
Lastdigit=c%pow(10,a)
if Lastdigit==n:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')