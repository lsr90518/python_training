#!/usr/bin/env python3
a = 10
b = 100
def oya():
    a = 1
    def foo():
        global a
        a = 2
        print(a)
        def ff():
            b = 3;
    foo()
    print(a, locals())


oya()
