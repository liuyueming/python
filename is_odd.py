def is_odd(n):
    return n%2==1

l=list(filter(is_odd,range(1,20)))
print(l)

l=list(filter(lambda n:n%2==1,range(1,20)))
print(l)
