n = int(input())
x = []
y = []

for i in range(n):
    a, b = (map(int, input().split()))
    x.append(a), y.append(b)

for i in range(n):
    rank = 1
    for j in range(n):
        if x[i] < x[j] and y[i] < y[j]:
            rank += 1
    print(rank, end=" ")
