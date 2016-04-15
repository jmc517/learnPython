#!python
# encoding: utf-8
import io
import cPickle as pickle

L=[]
for i in range(1,10):
    L.append(i)

d = L
f = open('dump.txt', 'wb')
pickle.dumps(int(d),f)
f.close()