a = input().split()
c = int(input())
h = int(a[0])
m = int(a[1])
t = 60*h+m+c
if t >=1440 :
    print(t//60-24, t%60) 
else :
    print(t//60, t%60)
