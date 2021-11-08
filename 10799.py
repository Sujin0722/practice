import sys

symbol = sys.stdin.readline()
arr = []
count = 0

for i in range(len(symbol)-1):
    if symbol[i] == '(':
        arr.append('(')
    else:
        if symbol[i-1] == '(':
            arr.pop()
            count += len(arr)
        else:
            arr.pop()
            count +=1

print(count)