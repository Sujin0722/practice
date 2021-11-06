n = int(input())
a = []

for i in range(n):
    x, y= map(int, input().split())
    a.append([x,y])

a.sort(key=lambda x:(x[1], x[0]))
# x[1]을 기준으로 먼저 정렬하고, x[0]기준으로 재정렬

for i in a:
    print(i[0], i[1])