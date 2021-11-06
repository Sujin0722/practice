import sys

arr = []
arr_2 = []
arr = list(input())
c = int(input())

for i in range(c):
    x = sys.stdin.readline().split()
    if x[0] == 'L' and arr != []:
            arr_2.append(arr.pop())
    elif x[0] == 'D' and arr_2 != []:
            arr.append(arr_2.pop())
    elif x[0] == 'B' and arr != []:
            arr.pop()
    elif x[0] == 'P':
        arr.append(x[1])

print(''.join(arr)+''.join(arr_2[::-1]))