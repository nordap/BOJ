def chk_pt(s):
    if len(s) == 0:
        return True
    
    if s[0:2] == '01':
        return chk_pt(s[2:len(s)])

    elif s[0:2] == '10':
        if len(s) == 2:
            return False
        i = 2
        cnt = 0
        while i<len(s) and s[i] == '0':
            i += 1
            cnt = 1
        if cnt == 0:
            return False

        cnt = 0
        while i<len(s) and s[i] == '1':
            i += 1
            cnt = 1
        if cnt == 0:
            return False

        return chk_pt(s[i:len(s)])
    else:
        return False



t = int(input())

for i in range(t):
    s = input()
    if chk_pt(s) is True:
        print('YES')
    else:
        print('NO')
    
