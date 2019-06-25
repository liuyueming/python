#构建以2开始的自然数序列
def _natural_iter():
    n=2
    while True:
        yield n
        n=n+1

#定义不能被整除函数
def _not_divisible(n):
    return lambda x:x%n>0

#定义素数函数
def primes():
    #把从2开始的自然数赋值给序列it
    it=_natural_iter()
    while True:
        #去序列第一个数一定是素数作为生成器的返回
        n=next(it)
        yield n
        #把序列的第一位数作为被除数依次使用后面的数如果能被整除则删除，不能被整除则保留
        #例如第一次使用filter过滤及把偶数过滤掉剩下的为从3开始的所有奇数
        it=filter(_not_divisible(n),it)

for n in primes():
    if n<100:
        print(n)
    else:
        break
