l = int(input())

for i in range(l):
    h,w,n = map(int,input().split(' '))

    a = h if n%h==0 else n%h
    b = n if h==1 else (int((n-1)/h)+1)

    room_num = a*100 + (b)
    print(room_num)
    
