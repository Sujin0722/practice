t=int(input())
tmp =1
count = 0
for i in range(1, t+1):
    tmp *= i

arr = list(str(tmp))

for i in range(len(arr)-1, -1, -1):
    if arr[i] == '0':
        count += 1
    else:
        print(count)
        break