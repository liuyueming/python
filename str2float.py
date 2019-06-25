from functools import reduce
def str2float(s):
    def fn(x,y):
        return x*10+y

    def char2num(s):
        digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        return digits[s]
    
    s1,s2=s.split('.') #字符串'123.456'使用.号分割后的列表为['123','456']分别赋值给s1 s2
    s1=reduce(fn,list(map(char2num,s1))) #由字符串'123'转换成整数123
    s2=reduce(fn,list(map(char2num,s2))) #由字符串'456'转换成整数456
    while s2>=1:                         #如果s2>=1
        s2=s2/10                         #则除以10取商一直到s2<1 最后s2=0.456浮点数
    
    return s1+s2			 #整数加小数作为函数结果返回

s=str2float('123.456')
print(s)
