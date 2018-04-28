def func():
    testcase = input().split(' ')
    n = int(testcase[0])
    s = testcase[1]

    result = ''

    for i in s:
        result += i*n

    print(result)

    
def a():
    n = int(input())
    for i in range(n):
        func()

if __name__ == "__main__":
    a()
