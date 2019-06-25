def check_code():
    import random
    checkcode = ''
    for i in range(4):
        current = random.randrange(0,4)
        if current != i:
            temp = chr(random.randint(65,90))
        else:
            temp = random.randint(0,9)
        checkcode += str(temp)
    return checkcode

while True:
    code = check_code()
    print(code)
    v = input('>>>')
    if v.upper() == code:
        print('You input is right')
    else:
        continue
 
