l = ['D','C','B','A','E']

for i in range(3):
    w,x,y,z = map(int,input().split(' '))
    
    s = sum([w,x,y,z])

    print(l[s])
              
