a = input()
old_num=a
C = 0
if int(old_num) < 10 :
    old_num = "0" + old_num
    a = old_num
while True :
    n = int(old_num[0]) + int(old_num[1])
    new_num = old_num[-1] + str(n)[-1]
    old_num = new_num
    C+=1
    if old_num == a :
        break
print(C)
