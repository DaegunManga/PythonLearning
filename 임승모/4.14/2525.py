def printresult(a,b):
    if a >= 24:
        print(a-24,b)
    else:
        print(a,b)



A, B = input().split()
A = int(A)
B = int(B)
C = int(input())

printresult(A + (B+C)//60, (B + C)%60)
