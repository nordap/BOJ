def a(n):
    count = 0
    for i in range(n):
        if func():
            count += 1
    return count

def func():
    s = input()
    #d = [0]*26
    d = list()
    
    #for i in range(len(s)-1):
    #    if s[i] != s[i+1]:
    #        if d[ord(s[i+1])-ord('a')] == 1:
    #            return False
    #    d[ord(s[i])-ord('a')] = 1
    
    for i in s:
        if d:
            if d[-1] != i:
                if i in d:
                    return False
                else:
                    d.append(i)
        else:
            d.append(i)

    return True

if __name__ == "__main__":
    print(a(int(input())))
