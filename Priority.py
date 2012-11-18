while(1):
    print "------------Implementation of Priority Algorithms for Bus Arbitration----------------"
    print "\n"
    print "Assumption : There is no parallelism in between the processes and all the processors are requesting use of the bus\n"
    a=input("Enter your choice :\n1- Static Priority Algorithm\n2- Dynamic Priority Algorithm\n3- To exit\n")
    if a not in range(1,4):
        print "\nInvalid Option\n"
    if a==3:
        break
    if a==1:
        print "\n"
        print "-------------Static Daisy Chain Algorithm Implementation-----------"
        print "\n"
        b=input("Enter number of Processors\n")
        print "Processors are numbered from 1 to",b
        print "\n"
        print "The Priority is based on the location of processors that is the processor which is numbered minimum is allocated maximum priority and so on..\n"
        c=input("Enter no of processes you want to have ?\n")
        print "\n"
        print "-----------------------------------------------------------------------"
        for i in range(1,c+1):
            print "Process -",i,"goes to processor -",1
            print "\n"
            print "Priority of processors is"
            for j in range(1,b+1):
                print j
            print "\n\n"
    if a==2:
        print "\n"
        print "------------Rotating Daisy Chain Algorithm Implementation----------"
        print "\n"
        print "Assumption : Instead of using any arbitration module , The initial priority is assumed to be same as that of Static Daisy Chain Priority Algorithm \n\n"
        b=input("Enter number of Processors\n")
        print "Processors are numbered from 1 to",b
        print "\n"
        print "This Priority is based on the LRU mechanism i.e. Least recently used device will get maximum priority or in other words Once one processor is used\n"
        c=input("Enter number of parallel processes you want to have ?\n")
        print "\n"
        print "--------------------------------------------------------------------------"
        for i in range(1,c+1):
            mo=i
            if i>b:
                mo=i-b
            print "priority of processors for the next process is"
            j=0
            j=j+i
            if j>b+1:
                j=j-b
            k=0
            while j<=b+1 and k<b:
                k=k+1
                if j==b+1:
                    j=j-b
                print j
                j=j+1
            print 
            print "Process -",i,"goes to processor -",mo
            print "\n\n\n"
