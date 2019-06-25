def is_palindrome(n):
    #str(n)把整数转换成字符串使用切片法反转
    #例如s='123'则s[::-1]='321'
    #如果反转后与反转前是一致则返回True
    return str(n)==str(n)[::-1]

#打印1-1999之间所有回数
print(list(filter(is_palindrome,range(1,2000))))
