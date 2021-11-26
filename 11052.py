n = int(input())
arr = [0]
arr+=list(map(int, input().split()))

d = [0]*(n+1)
d[1] = arr[1]
d[2] = min(arr[2], arr[1]*2)

for i in range(3, n+1):
    d[i] = arr[i]
    for j in range(1, i//2+1):
        d[i] = min(d[i], d[j]+d[i-j])

print(d[n])