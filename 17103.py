import sys

R = 100
arr=[False, False]+[True]*(R-2)

def prime_list(n):
    m=int(n**0.5)
    for i in range(2, m+1):
        if arr[i] == True: # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                arr[j] = False
    return [i for i in range(2, n) if arr[i]==True]

print(prime_list(R))
t= int(input())

for _ in range(t): #소수짝 찾기
    cnt=0
    n=int(sys.stdin.readline())
    for i in range((n//2)+1):
        if arr[i] and arr[n-i]:
            cnt+=1
    print(cnt)