#!/usr/bin/env python
import getpass
true_name = 'liuyueming'
true_passwd = 'pwd'
input_name = input('Please input your name:')
input_passwd = input('Please input your password:')
if input_name==true_name and input_passwd==true_passwd:
    print("Welcome",input_name)
else:
    print("Login failure")
