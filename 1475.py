n = int(input())

l = [0 for i in range(10)]

if n == 0:
    l[0] = 1

while(n is not 0):
    l[n%10] += 1
    n = n//10

sum = l[6] + l[9]
l[6] = l[9] = 0

print(max(int((sum+1)/2),max(l)))
