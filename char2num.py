#加载reduce模块
from functools import reduce
def fn(x,y):
    return x*10+y

#定义函数把字符串转换成数字参数为字符串‘1’，返回为整数1
def char2num(s):
    digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return digits[s]

s='13579'
print('需要转换成整数的字符串是',s)
#使用map函数生成迭代器，迭代后输出为[1,3,5,7,9]
l=map(char2num,s)
print('使用map转换后的生成器',l)
#使用reduce把生成的序列计算成整数
#计算过程为
#reduce(fn,[1,3,5,7,9])
#fn(fn(fn(fn(1,3),5),7),9)
#fn(fn(fn(13,5),7),9)
#fn(fn(135,7),9)
#fn(1357,9)
#13579
print(reduce(fn,l))
