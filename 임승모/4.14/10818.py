howmany = int(input())
N = list(map(int, input().split()))
N = N[0:howmany]

large_num = N[0]
small_num = N[0]
for i in N:
    if i >= large_num:
        large_num = i

for m in N:
    if m <= small_num:
        small_num = m

print(small_num, large_num)
