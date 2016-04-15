# encoding: UTF-8
def histogram(s):
    d=dict()
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return  d

def print_hist(h):
    for s in h:
        print(s,h[s])

print_hist(histogram('parrot'))