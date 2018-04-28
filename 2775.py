a = [[0 for i in range(15)] for j in range(15)]

for i in range(1,15):
	a[0][i] = i

for i in range(1,15):
	for j in range(1,15):
		a[i][j] = a[i][j-1] + a[i-1][j]

t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())

    print(a[k][n])
