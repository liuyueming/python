#加载reduce模块
from functools import reduce
def char2int(s):
    def fn(x,y):
        return x*10+y

#定义函数把字符串转换成数字参数为字符串‘1’，返回为整数1
    def char2num(s):
        digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        return digits[s]
    
    return(reduce(fn,map(char2num,s)))

s='13579'
print(char2int(s))
