def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b) #把n-1个盘子从 a 移动到 b
        move(1, a, b ,c)#把1个盘子从 a 移动到 c
        move(n-1, b, a, c)#把n-1个盘子从 b 移动到 c
                          #一直循环到n==1

move(2, 'A', 'B', 'C')
