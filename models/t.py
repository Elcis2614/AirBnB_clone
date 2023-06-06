#!/usr/bin/python3
class t():
    def __init__(self, **kargs):

        for key in kargs :
            self.__dict__[key] = kargs[key]

    def f(self,) :
        print (self.b)
d = {'a':1, 'b' : 2, 'c' : 3}
s = t(**d)
s.f()
