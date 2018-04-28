if __name__ == "__main__":
    scr = 0
    result = 0

    for i in range(5):
        scr = int(input())
        if scr < 40:
            scr = 40
        result += scr

    result = int(result/5)
    print(result)
    
