#!/usr/bin/python3
#from base_model import BaseModel
#d = BaseModel()
#print(type(d))
#my_dic = d.to_dict()
#print(d.to_dict())
s = {'name' : 'example', 'value': 2}
print("s = {}".format(s))
v = s.copy()
print("v copied = {}".format(v))
s['name'] = 'changed'
print("v after s changed = {} ".format(v))
