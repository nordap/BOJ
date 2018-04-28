if __name__ == "__main__":
    s = input()
    arr = [-1]*26
    pivot = ord('a')

    for i in range(len(s)):
        i_where = ord(s[i])-pivot
        if arr[i_where] == -1:
            arr[i_where] = i

    for i in arr:
        print(i)
