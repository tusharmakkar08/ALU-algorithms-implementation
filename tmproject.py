print "-----------------------Welcome to ALU unit of TM computer -------------------------"
while(1):
    cint=0
    cint=input("Enter :\n 1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division \n 5 for finding GCD \n 6 for exit \n");
    if(cint==6):
        break
    a=input("Enter 1st positive integer\n")
    b=input("Enter 2nd positive integer\n")
    m=bin(a)[2:].zfill(8)
    n=bin(b)[2:].zfill(8)
    global m
    global n
    def sub(a,b):
        i=7
        c=0
        while (i>=0):
            l=int(m[i])^int(n[i])^c
            k.append(str(l))
            c=(~int(m[i])&int(n[i]))|(int(n[i])&c)|(~int(m[i])&c)
            print "Difference is ",l,"and borrow is ",c
            i=i-1
        print "Final answer is ( in 2's compliment )","".join(k[::-1]),"in binary system and ",(a-b),"in decimal system"
        if a-b<0:
            i=7
            subi=[]
            while(i>=0):
                if k[i]=='0':
                    subi.append('1')
                if k[i]=='1':
                    subi.append('0')
                i=i-1
            i=7
            c=0
            t=[]
            lol=['0','0','0','0','0','0','0','1']
            while (i>=0):
                l=int(subi[i])^int(lol[i])^c
                t.append(str(l))
                c=(int(subi[i])&int(lol[i]))|(int(lol[i])&c)|(int(subi[i])&c)
                i=i-1
            print "Final answer is -","".join(t[::-1]),"in binary system"
        print "\n"
    k=[]
    print "CPU stores 1st number as",m
    print "CPU stores 2nd number as",n
    if cint==1:
        print "Implementing using full adder"
        i=7
        c=0
        while (i>=0):
            l=int(m[i])^int(n[i])^c
            k.append(str(l))
            c=(int(m[i])&int(n[i]))|(int(n[i])&c)|(int(m[i])&c)
            print "Sum is ",l,"and carry is ",c
            i=i-1
        print "Final answer is ","".join(k[::-1]),"in binary system and ",(a+b),"in decimal system \n"
    if cint==2:
        print "CPU basically does the addition of a and -b \n"
        print "Implementing using full subtractor\n"
        sub(a,b)
    if cint==3:
        print "Following Binary multiplication partial product procedure \n"
        i=7
        p=[]
        l=0
        mul=0
        while(i>=0):
            if(n[i]=='1'):
                p.append(((m+l*'0').zfill(16)))
            else:
                p.append((('00000000'+l*'0').zfill(16)))
            i=i-1
            l=l+1
        print "My partial products are :"
        for i in p:
            print i
            i=int(i,2)
            mul=mul+i
        print "Final Answer in Binary form is ",bin(mul)[2:].zfill(8),"and in decimal form is",mul,"\n"
    if cint==4:
        print "First implementing 2 fast division approaches\n\n"
        print "1 . Using Newton Raphson division algorithm \n"
        import mpmath
        from math import log
        START_PREC = 15
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
        print "\n\n2 . Following recursive approach "
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
        print "Quotient is ",div(a,b),"and remainder is ",r,"\n"
    if cint==5:
        def gcd(a,b):
            if a==b:
                print "GCD is",a,"and in binary form it is",bin(a)[2:].zfill(8)
                return a
            if a>b:
                print "Now",a,"is greater than",b
                sub(a,b)
                a=a-b
                b=b
                gcd(a,b)
            if b>a:
                print "Now",b,"is greater than",a
                sub(b,a)
                b=b-a
                a=a
                gcd(a,b)
        gcd(a,b)
        #print "GCD in binary form is",str(bin(int(gcd(a,b))))[2:].zfill(8),"and numerically it is",int(gcd(a,b))
    print "\n--------------------------------------------------------------------------------------\n"
