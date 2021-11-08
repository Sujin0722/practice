import sys

n=int(input())
arr=list(map(int, sys.stdin.readline().split()))
output=[-1]*n
stack = []

stack.append(0)
for i in range(1, n):
    print(arr[stack[-1]], arr[i])
    while stack and arr[stack[-1]]<arr[i]:
        output[stack.pop()] = arr[i]
    stack.append(i)
print(" ".join(map(str, output)))