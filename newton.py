import mpmath
from math import log
START_PREC = 15
a=input("Enter 1st positive integer\n")
b=input("Enter 2nd positive integer\n")
def size(x):
    if isinstance(x, (int, long)):
        return int(log(x,2))
    return x.numdigits(2)
def newdiv(p, q):
    szp = size(p)
    szq = size(q)
    szr = szp - szq
    if min(szp, szq, szr) < 2*START_PREC:
        return p//q
    r = (1 << (2*START_PREC)) // (q >> (szq - START_PREC))
    last_prec = START_PREC
    for prec in giant_steps(START_PREC, szr):
        a = lshift(r, prec-last_prec+1)
        b = rshift(r**2 * rshift(q, szq-prec), 2*last_prec)
        r = a - b
        last_prec = prec
        return ((p >> szq) * r) >> szr
print "Final answer is quotient",bin(newdiv(a,b))[2:].zfill(8)," and remainder in binary form is",bin(a%b)[2:].zfill(8),"\nquotient in decimal form is ",a/b," and ",a%b," is remainder in decimal form\n"

