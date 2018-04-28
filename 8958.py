def a(n):
    for i in range(n):
        func();

def func():
    str = input();
    scr = 0
    result = 0;
    for i in str:
        if i == 'O':
            scr += 1
            result += scr
        elif i == 'X':
            scr = 0
    print(result)
            

if __name__ == "__main__":
    i = int(input())
    
    a(i)
    
