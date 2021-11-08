import sys
from collections import Counter

n = int(input())
arr=sys.stdin.readline().split()
tmp=Counter(arr)
output=[-1]*n
stack=[]

stack.append(0)
for i in range(1, n):
    while stack and tmp[arr[stack[-1]]]<tmp[arr[i]]:
        output[stack.pop()] = arr[i]
    stack.append(i)

print(' '.join(map(str, output)))