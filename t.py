#!/usr/bin/python3
class a():
    name = ""
    gender = ""

    def f(self):
        print(self.name)

    def p(self):
        return(self.__dict__)

x = a()
x.name = "sammy"
x.gender = " Male"
print(x.p())
s = a()
s.name = "Chris"
print(s.p())
