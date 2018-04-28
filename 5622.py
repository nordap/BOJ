num = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]

a = input()

sum = 0

for i in a:
    sum += (num[ord(i)-65]+1)

print (sum)
