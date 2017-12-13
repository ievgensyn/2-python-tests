# -*- coding: utf-8 -*-

def greeting():
    lst = [raw_input().split() for i in range(int(raw_input()))]
    lst.sort(key=lambda i: i[-1])
    for i in lst:
        if i[-2] == u'М'.encode('utf-8'):
            print "Г-н", " ".join(i[0:2])
        else:
            print "Г-жа", " ".join(i[0:2])

greeting()
