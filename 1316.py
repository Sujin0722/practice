N = int(input())
count = N

for i in range(N):
    arr = list(input())
    for j in range(len(arr)-1):
        if arr[j]==arr[j+1]:
            pass
        elif arr[j] in arr[j+1:]:
            count -= 1
            break
print(count)
