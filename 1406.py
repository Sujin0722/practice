import sys

arr = []
arr = list(input())
c = int(input())
point = len(arr)

for i in range(c):
    x = sys.stdin.readline().split()
    if x[0] == 'L':
        if point != 0:
            point -= 1
    elif x[0] == 'D':
        if point != len(arr):
            point += 1
    elif x[0] == 'B':
        if point != 0:
            del arr[point-1]
            point -= 1
    else:
        arr.insert(point, x[1])
        point += 1

print(''.join(arr))