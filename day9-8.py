#!/usr/bin/env python
count=0
while count<3:
    user=input('>>>')
    pwd=input('>>>')
    if user=='liuyueming' and pwd=='123':
        print('Welcome')
        break
    else:
        print('Login failure')
    count=count+1
