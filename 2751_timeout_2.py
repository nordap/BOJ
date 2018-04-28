import sys

def merge(a, start, m, end):
    temp = []
    x,y = start, m

    while x < m and y < end:
        if a[x] < a[y]:
            temp.append(a[x])
            x = x+1
        else:
            temp.append(a[y])
            y = y+1

    i = x
    while i < m:
        temp.append(a[i])
        i = i+1
    i = y
    while i < end:
        temp.append(a[i])
        i = i+1
    a[start:end] = temp
    return a


def merge_sort(l):
    size_l = len(l)
    t = 1
    while(t < size_l):
        i = 0
        while(i < size_l):
            start = i
            end = min(i + (t*2), size_l)
            m = min(i+t, end)

            l = merge(l, start, m, end)

            i = i + (t*2)

        t = t*2

    return l



n = int(input())
l = list()

for i in range(n):
    l.append(int(sys.stdin.readline().rstrip()))

result = merge_sort(l)

for i in result:
    print (i)

