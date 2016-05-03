#!python
# encoding: utf-8
f=open('words.txt','r')
result = list()
for line in f.readlines():
     line = line.strip()
     result.append(line)
print ','.join(result)