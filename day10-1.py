content=input('Pleast input')
letter_count = 0
number_count = 0
for item in content:
    if item.isalpha():
        letter_count = letter_count + 1
    elif item.isdigit():
        number_count = number_count + 1
print('字母数为:',letter_count)
print('数字数为:',number_count)
