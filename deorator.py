import time 
import functools

def timeit(func):
    @functools.wraps(func)
    def test(*args,**kw):
        start=time.time()
        func(*args,**kw)
        end=time.time()
        print('Time used:',end-start)
        #return func(*args,**kw)
    return test

@timeit
def sum1(s):
    print(s)

sum1('hello world')
print('函数名为',sum1.__name__)
