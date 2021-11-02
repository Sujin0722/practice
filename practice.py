import sys

n = int(input())
arr = []
check = []

for i in range(n):
    a=0
    vps = list(input())
    for j in vps:
        if j=='(':
            check.append('(')
        elif j==')' and len(check) != 0:
            check.pop()
        elif j==')' and len(check) <= 0:
            a=-1
            break
    if a != -1 and len(check) == 0:
        print("YES")
    elif a == -1 or len(check)!=0:
        print("NO")
    check.clear()