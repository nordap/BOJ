def find_run_time(n):
    i = 1
    cnt = 0
    while (n > i*2):
        n = n-(i*2)
        cnt +=2
        i += 1
    if n>i:
        cnt += 2
    elif n>0:
        cnt += 1

    print(cnt)

n = int(input())

for i in range(n):
    s = input()

    a = int(s.split(' ')[0])
    b = int(s.split(' ')[1])
    
    
    find_run_time(b-a)
    
    
