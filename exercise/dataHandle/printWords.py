# -*- coding: utf-8 -*-

fin=open('words.txt')
for i in fin:
    word=i.strip()
    if len(word)>20:
        print(word)