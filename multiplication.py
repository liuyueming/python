def product(*args):
    y=1
    for x in args:
        y=y*x
    return y

print(product(2,3,5))
