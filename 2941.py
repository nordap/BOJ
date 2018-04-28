ca = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

a = input()

result = 0

for i in range(8):
    a = a.replace(ca[i], str(i))

result = len(a)

print (result)
