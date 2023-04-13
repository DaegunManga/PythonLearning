h, m = map(int, input().split())
add = int(input())

hour = (m+add)//60
min = (m+add)%60

if(m + add >= 60):
  if(h+hour >= 24):
    h = h - 24
  h = h + hour
  print(h, min)

else:
  if(h >= 24):
    h = h - 24
  print(h, m+add)
