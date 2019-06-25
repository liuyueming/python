def trim(s):
    l=''
    for i in range(len(s)):
        if s[i] == ' ':
          pass
        else:
          l=l+s[i]
    return l

print(trim('  askdj  '))
