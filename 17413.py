import sys

t = sys.stdin.readline()
tmp = []
symbol = []
reverse = []
output = []

def reversed():
    while len(reverse) != 0:
        output.append(reverse.pop())

for i in range(len(t)-1):
    if t[i] == '<':
        symbol.append('<')
        reversed()
        output.append('<')
    elif t[i] == '>':
        symbol.pop()
        output.append('>')
    elif len(symbol) != 0:
        output.append(t[i])
    elif len(symbol) == 0 and t[i] != ' ':
        reverse.append(t[i])
    elif t[i] == ' ':
        reversed()
        output.append(t[i])
    elif i == len(t)-1:
        reversed()

if len(reverse) != 0:
    reversed()

for i in output:
    print(i, end='')