import sys

n=int(input())
exp = input()
tmp = "+-*/"
stack = []
abc = []

for i in range(n):
    abc.append(int(input()))


for i in exp:
    if i.isupper():
        print(i)
        stack.append(abc[ord(i)-ord('A')])
    else:
        num2 = stack.pop()
        num1 = stack.pop()
        if i == '+':
            stack.append(num1 + num2)
        elif i == '-':
            stack.append(num1 - num2)
        elif i == '*':
            stack.append(num1 * num2)
        elif i == '/':
            stack.append(num1 / num2)

print("%.2f" %stack[0])