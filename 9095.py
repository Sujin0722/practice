t=int(input())
d=[0,1,2,4]

for j in range(4, 12):
    d.append(d[j - 3] + d[j - 2] + d[j - 1])

for i in range(t):
    n = int(input())
    print(d[n])