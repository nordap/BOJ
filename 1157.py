if __name__ == "__main__":
    s = input()
    upper_s = s.upper()
    d = dict()
    
    for i in upper_s:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1

    max_key = '0'
    max_value = -1
    for i in d.keys():
        if d[i] > max_value:
            max_value = d[i]
            max_key = i

    d.pop(max_key)

    if max_value in d.values():
        print("?")
    else:
        print(max_key)
