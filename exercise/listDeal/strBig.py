#!python
# encoding: utf-8
import string

b=raw_input('输入一个包含大小写的字符,串返回一个只有大写的字符串\n')
def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res
print(''.join(only_upper(b)))

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.upper())
    return res
a=raw_input('请输入')
print(capitalize_all(a))