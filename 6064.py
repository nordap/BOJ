def gcd(a,b):
    while b>0:
        a,b = b, a%b
    return a


numOfcase = int(input())


for cnt in range(numOfcase):
    s = input()
    
    m,n,x,y = map(int,s.split(' '))

#    g = gcd(m,n)
#    l = m*n/g
#
#    a,b = (0,0)
#    t = 0

    if ((x-y)%g) != 0:
        result = -1
    else:
        r0 = 
        
#        for i in range(int(l/m+1)):
#            if (i*m+x-y)%n == 0:
#                a = i
#                break
#        result = a*m + x
        
    print (result)
