#!python
# encoding: utf-8
from string import maketrans   # 必须调用 maketrans 函数。

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)
str='abcd'
print str.translate(trantab);