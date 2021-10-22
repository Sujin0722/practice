arr = list(input())
count = 0

for i in range(len(arr)):
    if arr[i]=='c':
        if arr[i+1] == '=':
            ++count
        elif arr[i+1] == '-':
            ++count

    elif arr[i]=='d':
        if arr[i+1] == 'z':
            ++count
            arr.pop(i), arr.pop(i+1),arr.pop(i+2)
            continue
        elif arr[i+1] == '-':
            ++count

    elif arr[i]=='l' or 'n':
        if arr[i+1] == 'j':
            ++count

    elif arr[i]=='s' or 'z':
        if arr[i+1] == '=':
            ++count

    arr.pop(i), arr.pop(i + 1)
    print(arr)
