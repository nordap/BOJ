import math

def when_fight(N,x,y):
    x,y = min(x,y),max(x,y)
    n = math.ceil(math.log(N,2))
    low = 0
    high = int(pow(2,n))

    for i in range(n):
        m = (high+low)//2

        if x <= m and y > m:
            return n-i
        
        elif x <= m and y <= m:
            low = low
            high = m
            i += 1
            
        elif x > m and y > m:
            low = m
            high = high
            i += 1
            
        else:
            return -1  

N,x,y = map(int,input().split(' '))

print (when_fight(N,x,y))
        
        
