if __name__ == "__main__":
    s = input()
    s = s.upper()
    d = dict()
    
    #for i in upper_s:
    #    if i in d.keys():
    #        d[i] += 1
    #    else:
    #        d[i] = 1

    for i in range(ord('A'),ord('Z')+1):
        d[chr(i)] = s.count(chr(i))            

    chk = 0
    max_key = '0'
    max_value = -1
    for i in d.keys():
        if d[i] > max_value:
            max_value = d[i]
            max_key = i
            chk = 0
        elif d[i] == max_value:
            chk = 1

    if chk:
        print("?")
    else:
        print(max_key)
