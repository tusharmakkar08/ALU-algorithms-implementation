a=input()
b=input()
m=bin(a)[2:].zfill(8)
n=bin(b)[2:].zfill(8)
def div(a,b):
    q=1
    global r
    if(a==b):
        r=0
        return 1
    elif(a<b):
        r=a
        return 0
    while b<=a:
        b=b<<1
        q=q<<1
    b=b>>1
    q=q>>1
    q=q+div(a-b,b)
    return q
print div(a,b),r
