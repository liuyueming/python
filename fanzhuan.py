s='helloworld'
#1切片法最常用
r=s[::-1]
print('切片法',r)

#2使用reduce
from functools import reduce
#匿名函数，冒号前面为参数，冒号后为返回结果
#第一步x='h',y='e'返回字符串'eh'把这个结果作为新的参数x='eh' y='l' 结果为leh依次类推就把字符串反转了
r=reduce(lambda x,y:y+x,s)
print('reduce函数',r)

#3使用递归函数
def func(s):
    if len(s)<1:
        return s
    return func(s[1:])+s[0]

r=func(s)
print('递归函数法',r)

#4使用栈
def func(s):
    l=list(s)
    result=''
    #把字符串转换成列表pop()方法删除最后一个元素并把该元素作为返回值
    while len(l):
        result=result+l.pop()
    return result

r=func(s)
print('使用栈法',r)

#5for循环
def func(s):
    result=''
    max_index=len(s)
    #for循环通过下标从最后依次返回元素
    for index in range(0,max_index):
        result=result+s[max_index-index-1]
    return result

r=func(s)
print('使用for循环法',r)

#6使用列表reverse法
l=list(s)
#reverse方法把列表反向排列
l.reverse()
#join方法把列表组合成字符串
r="".join(l)
print('使用列表reverse法',r)
