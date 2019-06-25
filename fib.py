def fib(max):
    n,a,b=0,0,1
    while n<max:
        #print(b)
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'

print(fib(1))
for x in fib(1):
    print(x)
print(fib(2))
for x in fib(2):
    print(x)
print(fib(3))
for x in fib(3):
    print(x)
print(fib(4))
for x in fib(4):
    print(x)
print(fib(5))
for x in fib(5):
    print(x)
