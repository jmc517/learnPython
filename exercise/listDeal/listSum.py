#!python
# encoding: utf-8

t = [[1, 2], [3], [4, 5, 6]]
def nested_sum(t):
    total=0
    for i in t:
        total += sum(i)
    return  total

t1 = [1, 2, 3]
def cumsum(t1):
    total=0
    res=[]
    for i in t1:
        total += i
        res.append(total)
    return res

t2 = [1, 2, 3, 4]
def middle(t2):
    return t2[1:-1]

all=nested_sum(t)
all1=cumsum(t1)
all2=middle(t2)

print(all)
print(all1)
print(all2)