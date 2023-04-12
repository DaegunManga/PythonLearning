n = int(input())
for i in range (n) :
    L = list(map(int,input().split()))
    L1 = L[1:]
    N = L[0]
    avr = sum(L1) / N
    n1 = 0
    for a in L1 :
        if a > avr :
            n1 +=1
    ans = "{:.3f}".format(round((n1/N)*100,3))
    print(str(ans) + "%")
