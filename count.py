def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        #把函数f地址追加至列表fs
        fs.append(f)
    #返回为一个包含3个函数f地址的列表
    return fs

print('count函数返回一个列表，列表分别为函数f地址',count())
f1,f2,f3 = count()
print(f1,'f1执行结果是',f1())
print(f2,'f2执行结果是',f2())
print(f3,'f3执行结果是',f3())
