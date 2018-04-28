import sys

n = int(input())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline().rstrip()))
    
for i in sorted(l, reverse = True):
    print (i)
