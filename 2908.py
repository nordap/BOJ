if __name__ == "__main__":
    s = input()
    ss = s.split(' ')
    n1 = int(ss[0][2]+ss[0][1]+ss[0][0])
    n2 = int(ss[1][2]+ss[1][1]+ss[1][0])

    print(n1) if n1 > n2 else print(n2)
    
    
    #if int(n1[2]) > int(n2[2]):
    #    max = n1
    #elif int(n2[2]) > int(n1[2]):
    #    max = n2
    #else:
    #    if int(n1[1]) > int(n2[1]):
    #        max = n1
    #    elif int(n2[1]) > int(n1[1]):
    #        max = n2
    #    else:
    #        if int(n1[0]) > int(n2[0]):
    #            max = n1
    #        elif int(n2[0]) > int(n1[0]):
    #            max = n2

    #print(max[2]+max[1]+max[0])
