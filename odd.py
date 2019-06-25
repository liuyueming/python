def odd():
    n=2
    while True:
        yield n
        n=n+1

f=odd()
print(f)
for i in f:
    if i<100:
        print(i)
