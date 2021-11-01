n, m = map(int, input().split())
check = []
a = []

for i in range(n):
    check.append((input()))


for i in range(n-7): #세로
    for j in range(m-7): #가로
        w = 0
        b = 0
        for k in range(i, i+8):
            for t in range(j, j+8):
                if (k+t)%2 == 0: #짝수
                    if check[k][t] != 'W':
                        w+=1
                    elif check[k][t] != 'B':
                        b+=1
                else:
                    if check[k][t] != 'W':
                        b+=1
                    elif check[k][t] != 'B':
                        w+=1
        a.append(w)
        a.append(b)

print(min(a))