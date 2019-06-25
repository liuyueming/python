def triangles():
  L=[1]
  while True:
    yield L
    L=[1]+[L[i]+L[i+1] for i in range(len(L)-1)]+[1]

for x in triangles():
  print(x)
