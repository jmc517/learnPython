#!python
# encoding: utf-8
import datetime

t=datetime.datetime.now().strftime('%c')
print('今天是%s'%t)
a=raw_input('请输入一个字符串\n')
length=len(a)
print('该字符串长度是%s'%length)

for i in a:

    if a=='done':
        print('您输入了非法字符串%s'%a)
        break
    print([i])

while length>0:

last=a[length-1]