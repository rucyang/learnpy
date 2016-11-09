# ! /usr/bin/env python
# ! -*- coding:utf-8 -*-

try:
    import cPickle as pickle
except ImportError:
    import pickle

# d = dict(name = "Bob", age = 20, score = 100)

# with open('test.txt', "wb") as f:
# 	pickle.dump(d, f)


with open("test.txt", "rb") as f:
    d = pickle.load(f)

print(d)

