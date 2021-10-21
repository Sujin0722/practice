A, B= input().split()

A_l = list(A)
B_l = list(B)

A = int(A_l[2])*100+int(A_l[1])*10+int(A_l[0])
B = int(B_l[2])*100+int(B_l[1])*10+int(B_l[0])

if A>B:
    print(A)
else:
    print(B)