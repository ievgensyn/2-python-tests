# -*- coding: utf-8 -*-

# def sorting(contacts):
#     def wrapped():
#         return contacts().sort(key = lambda i: i[-1])
#     return wrapped

def greeting():
    lst = [raw_input().split() for i in range(int(raw_input()))]
    lst.sort(key=lambda i: i[-1])
    for i in lst:
        if i[-4] == u'М':
            print "Г-жа", " ".join(i[0:2])
        else:
            print "Г-н", " ".join(i[0:2])


greeting()
