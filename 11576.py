import sys

A, B = map(int, input().split())
n = int(input())
tmp = sys.stdin.readline().split()

arr = []
check = 0
count=0

for i in tmp[::-1]:
    count += int(i)*A**check
    check+=1

while count!=0:
    arr.append(str(count%B))
    count//=B

print(' '.join(arr[::-1]))