def func(arr):
    if arr == '1 2 3 4 5 6 7 8':
        print("ascending")
    elif arr == '8 7 6 5 4 3 2 1':
        print("descending")
    else:
        print("mixed")

if __name__ == "__main__":
    arr = input()
    
    func(arr)
