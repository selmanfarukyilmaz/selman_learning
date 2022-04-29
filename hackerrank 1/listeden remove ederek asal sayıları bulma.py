x = (int(input()) + 1)
sayılar = [i for i in range(2,x)]


for i in sayılar:
  # print(i,"ana sayılarım")
  for x in range (2,i):
    # print(x,"x")
    if i%x == 0:
      try:
        sayılar.remove(i)
        sayılar.insert(0,0)
      except:
        True
    else:
      continue
sayılar = set(sayılar)
sayılar = list(sayılar)
sayılar.sort()
sayılar.remove(0)
print(sayılar)


