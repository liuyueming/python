L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
#函数返回第一个元素名字
def by_name(t):
    m=t[0]
    return m

#函数返回第二个元素成绩
def by_score(t):
    n=t[1]
    return n

L1=sorted(L,key=by_name)
L2=sorted(L,key=by_score,reverse=True)
print(L1)
print(L2)
