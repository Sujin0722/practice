arr = input()
exp=[]
stack=[]

def popping():
    while len(exp)!= 0 and exp[-1] != '(':
        stack.append(exp.pop())
    if len(exp)!= 0 and exp[-1] == '(':
        exp.pop()

for i in range(len(arr)):
    if arr[i].isupper():
        stack.append(arr[i])
        if len(exp)!=0 and (exp[-1] == '*' or exp[-1] == '/'):
            popping()
    else:
        if arr[i] == '+':
            exp.append('+')
        elif arr[i] == '-':
            exp.append('-')
        elif arr[i] == '*':
            exp.append('*')
        elif arr[i] == '/':
            exp.append('/')
        elif arr[i] == '(':
            exp.append('(')
        elif arr[i] == ')':
            popping()

popping()
print(''.join(stack))
