n = int(input())
arr = []
stack = []
symbol = []
flag = 1
count = 1
for i in range(n):
    arr.append(int(input()))

for j in arr:
    for k in range(flag, j+1):
        stack.append(k)
        symbol.append("+")
        count+=1
    flag=count
    if stack[len(stack)-1] == j:
        stack.pop()
        symbol.append("-")
    else:
        print("NO")
        flag = -1
        break

if flag != -1:
    for i in symbol:
        print(i)