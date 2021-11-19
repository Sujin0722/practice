n, m= map(int, input().split())
top=1
down=1
count=0
for i in range(1, m+1):
    down *= i

for i in range(n-m+1, n+1):
    top *= i

final = list(str(top//down))

for i in range(len(final)-1, -1, -1):
    if final[i] == '0':
        count+=1
    else:
        print(count)
        break
