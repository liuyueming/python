#!/usr/local/python3/bin/python3
m=input("input a num:")
n=int(m)
print("你输入的是",n,"下面为你打印一个等腰三角形")
for i in range(1,n+1):
    for space in range(n-i):
        print (' ',end='')
    for star in range(2*i-1):
        print ('*',end='')
    print()
for i in range(1,n+1):
    for star in range(2*i-1):
        print ('*',end='')
    for space in range(n-i):
        print (' ',end='')
    print()


