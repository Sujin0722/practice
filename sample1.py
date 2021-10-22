num = list(input())
alpha = ['ABC', 'DEF','GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
count = 0

for i in range(len(num)):
    for j in range(len(alpha)):
        if num[i] in alpha[j]:
            count = count+(j+3)

print(count)