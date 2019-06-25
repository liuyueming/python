def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n

def _not_divisible(n):
    def f(x):
        return x%n>0
    return f

def primes():
    yield 2
    it=_odd_iter()
    while True:
        n=next(it)
        yield n
        it=filter(_not_divisible(n),it)
 
for n in primes():
    if n<100:
        print(n)
    else:
        break   
