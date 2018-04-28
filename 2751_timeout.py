def merge_sort(a):
    if len(a) == 1:
        return a
    
    l = merge_sort(a[0:len(a)//2])
    r = merge_sort(a[len(a)//2:len(a)])
 
    x = 0
    y = 0

    s = []
    
    while(1):
        if x == len(l):
            s += r[y:len(r)]
            break
        elif y == len(r):
            s += l[x:len(l)]
            break
        else:
            if l[x]<r[y]:
                s.append(l[x])
                x += 1
            else:
                s.append(r[y])
                y += 1

    return s

n = int(input())
a = []

for i in range(n):
    a.append(int(input()))
             
s = merge_sort(a)

print (s)
