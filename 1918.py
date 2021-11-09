arr = input()
priority = {'*':3, '/':3, '+':2, '-':2}
stack=[]
final = []

for i in range(len(arr)):
    if arr[i].isupper():
        final.append(arr[i])
    else:
        if arr[i] == '(':
            stack.append('(')
        elif arr[i] == '*' or arr[i] == '/':
            while stack and (stack[-1] =='*' or stack[-1] == '/'):
                final.append(stack.pop())
            stack.append(arr[i])
        elif arr[i] == '+' or arr[i] == '-':
            while stack and stack[-1] !='(':
                final.append(stack.pop())
            stack.append(arr[i])
        elif arr[i] == ')':
            while stack and stack[-1] !='(':
                final.append(stack.pop())
            stack.pop()

while stack:
    final.append(stack.pop())

print(''.join(final))
