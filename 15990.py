mod = 1000000009
max = 100000

# 앞이 가로 길이, 뒤가 세로 길이]
d=[[0]*4 for _ in range(max+1)]

# d[i][j] : i를 만드는 데 더해지는 끝 수가 j인 경우의 수
d[1] = [0,1,0,0]
d[2] = [0,0,1,0]
d[3] = [0,1,1,1]

for i in range(4,max+1):
    d[i][1] = d[i-1][2] + d[i-1][3]
    d[i][2] = d[i-2][1] + d[i-2][3]
    d[i][3] = d[i-3][1] + d[i-3][2]

    d[i][1] %= mod
    d[i][2] %= mod
    d[i][3] %= mod

t = int(input())

for j in range(t):
    n=int(input())
    print(sum(d[n])%mod)