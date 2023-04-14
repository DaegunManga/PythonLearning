A,B= input().split()
A,B = int(A), int(B)
C = int(input())
time = A*60+B+C
if time>=1440: 
    time = time-1440

print(time//60, time%60)
