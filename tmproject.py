print "-----------------------Welcome to ALU unit of TM computer -------------------------"
while(1):
    cint=0
    cmain=0
    clog=0
    cmain=input("Enter :\n 1 for Logical Unit \n 2 for Arithematic Unit\n 3 for exit\n")
    if cmain not in range(1,4):
        print "\nInvalid Option\n"
    if cmain==3:
        break
    if cmain==2:
        cint=input("Enter :\n 1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division \n 5 for finding GCD \n 6 for exit \n")
        if(cint==6):
            break
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
        if cint==1:
            a=input("Enter 1st positive integer\n")
            b=input("Enter 2nd positive integer\n")
            m=bin(a)[2:].zfill(8)
            n=bin(b)[2:].zfill(8)
            print "CPU stores 1st number as",m
            print "CPU stores 2nd number as",n
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
            a=input("Enter 1st positive integer\n")
            b=input("Enter 2nd positive integer\n")
            m=bin(a)[2:].zfill(8)
            n=bin(b)[2:].zfill(8)
            print "CPU stores 1st number as",m
            print "CPU stores 2nd number as",n
            print "CPU basically does the addition of a and -b \n"
            print "Implementing using full subtractor\n"
            sub(a,b)
        if cint==3:
            a=input("Enter 1st positive integer\n")
            b=input("Enter 2nd positive integer\n")
            m=bin(a)[2:].zfill(8)
            n=bin(b)[2:].zfill(8)
            print "CPU stores 1st number as",m
            print "CPU stores 2nd number as",n
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
            a=input("Enter 1st positive integer\n")
            b=input("Enter 2nd positive integer\n")
            m=bin(a)[2:].zfill(8)
            n=bin(b)[2:].zfill(8)
            print "CPU stores 1st number as",m
            print "CPU stores 2nd number as",n
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
            a=input("Enter 1st positive integer\n")
            b=input("Enter 2nd positive integer\n")
            m=bin(a)[2:].zfill(8)
            n=bin(b)[2:].zfill(8)
            print "CPU stores 1st number as",m
            print "CPU stores 2nd number as",n
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
        if cint not in range(1,7):
            print "\nInvalid Option\n"
    if cmain==1:
        clog=input("Enter : \n 1 : For 'OR' operator\n 2 : For 'AND' operator\n 3 : For 'NOT' operator\n 4 : For 'NAND' operator\n 5 : For 'NOR' operator\n 6 : For 'XOR' operator\n 7 : For 'XNOR' operator\n 8 : For right shifting the bits \n 9 : For Left Shifting the bits \n 10 : Exit \n")
        if clog not in range(1,11):
            print "\nInvalid Statement\n"
        if clog==10:
            break
        if clog==2:
            a=input("Enter 1st positive integer\n")
            b=input("Enter 2nd positive integer\n")
            m=bin(a)[2:].zfill(8)
            n=bin(b)[2:].zfill(8)
            print "CPU stores 1st number as",m
            print "CPU stores 2nd number as",n
            i=7
            addi=[]
            while i>=0:
                add=int(m[i])&int(n[i])
                print "And operation for bits yields ",add
                addi.append(str(add))
                i=i-1
            print "In Binary form And of ",a,"and",b,"is",''.join(addi[::-1]),"And in decimal form it is",a&b
        if clog==1:
            a=input("Enter 1st positive integer\n")
            b=input("Enter 2nd positive integer\n")
            m=bin(a)[2:].zfill(8)
            n=bin(b)[2:].zfill(8)
            print "CPU stores 1st number as",m
            print "CPU stores 2nd number as",n
            i=7
            addi=[]
            while i>=0:
                add=int(m[i])|int(n[i])
                print "OR operation for bits yields ",add
                addi.append(str(add))
                i=i-1
            print "In Binary form OR of ",a,"and",b,"is",''.join(addi[::-1]),"And in decimal form it is",a|b
        if clog==3:
            a=input("Enter  positive integer\n")
            m=bin(a)[2:].zfill(8)
            print "CPU stores  number as",m
            i=0
            addi=[]
            while i<=7:
                if m[i]=='0':
                    print "0 converted into 1"
                    addi.append("1")
                elif m[i]=='1':
                    print "1 converted into 0"
                    addi.append("0")
                i=i+1
            print "In binary form Not(compliment) of",a,"is",''.join(addi)
        if clog==4:
            a=input("Enter 1st positive integer\n")
            b=input("Enter 2nd positive integer\n")
            m=bin(a)[2:].zfill(8)
            n=bin(b)[2:].zfill(8)
            print "CPU stores 1st number as",m
            print "CPU stores 2nd number as",n
            i=7
            addi1=[]
            while i>=0:
                add=int(m[i])&int(n[i])
                print "And operation for bits yields ",add
                addi1.append(str(add))
                i=i-1
            i=7
            addi=[]
            while i>=0:
                if addi1[i]=='0':
                    print "0 converted into 1"
                    addi.append("1")
                elif addi1[i]=='1':
                    print "1 converted into 0"
                    addi.append("0")
                i=i-1
            print "In Binary form the NAND is",''.join(addi)
        if clog==5:
            a=input("Enter 1st positive integer\n")
            b=input("Enter 2nd positive integer\n")
            m=bin(a)[2:].zfill(8)
            n=bin(b)[2:].zfill(8)
            print "CPU stores 1st number as",m
            print "CPU stores 2nd number as",n
            i=7
            addi1=[]
            while i>=0:
                add=int(m[i])|int(n[i])
                print "OR operation for bits yields ",add
                addi1.append(str(add))
                i=i-1
            i=7
            addi=[]
            while i>=0:
                if addi1[i]=='0':
                    print "0 converted into 1"
                    addi.append("1")
                elif addi1[i]=='1':
                    print "1 converted into 0"
                    addi.append("0")
                i=i-1
            print "In Binary form the NOR is",''.join(addi)            
        if clog==6:
            a=input("Enter 1st positive integer\n")
            b=input("Enter 2nd positive integer\n")
            m=bin(a)[2:].zfill(8)
            n=bin(b)[2:].zfill(8)
            print "CPU stores 1st number as",m
            print "CPU stores 2nd number as",n
            i=0
            addi1=[]
            while(i<=7):
                add=int(m[i])^int(n[i])
                print "XOR operation on bits yiels",add
                addi1.append(str(add))
                i=i+1
            print "In binary form the XOR is",''.join(addi1)
        if clog==7:
            a=input("Enter 1st positive integer\n")
            b=input("Enter 2nd positive integer\n")
            m=bin(a)[2:].zfill(8)
            n=bin(b)[2:].zfill(8)
            print "CPU stores 1st number as",m
            print "CPU stores 2nd number as",n
            i=0
            addi1=[]
            while(i<=7):
                add=int(m[i])^int(n[i])
                print "XOR operation on bits yiels",add
                if add==0:
                    print '0 converted into 1'
                    add=1
                else:
                    print '1 converted into 0'
                    add=0
                addi1.append(str(add))
                i=i+1
            print 'In Binary form XOR is',''.join(addi1)
        if clog==8:
            a=input("Enter positive number\n")
            m=bin(a)[2:].zfill(8)
            print "CPU stores the number as",m
            print "It is done by using shift registers"
            i=0
            k=[]
            while i<=7:
                if i!=0:
                    lol=m[i-1]
                    k.append(str(lol))
                else:
                    k.append('0')
                i=i+1
            print "Right shifting a yields",''.join(k),"as binary and",a>>1,"as decimal"
        if clog==9:
            a=input("Enter positive number\n")
            m=bin(a)[2:].zfill(8)
            print "CPU stores the number as",m
            print "It is done by using shift registers"
            i=0
            k=[]
            while i<=7:
                if i!=7:
                    lol=m[i+1]
                    k.append(str(lol))
                else:
                    k.append("0")
                i=i+1
            print "Left shifting ",a," yields",''.join(k),"as binary and",a<<1,"as decimal"
    print "\n\n--------------------------------------------------------------------------------------\n\n"
