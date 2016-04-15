#!python
# encoding: utf-8

a=raw_input('请输入一个字符串\n')
b=dict()
for s in a:
    if s not in b:
        b[s]=1
    else:
        b[s] +=1
print(b)