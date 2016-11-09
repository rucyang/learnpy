#! /usr/bin/env python
#! -*- coding:utf-8 -*-

import json

d = dict(name = "Bob", age = 20, score = 100)
print json.dumps(d)

with open('test.txt', "wb") as f:
	json.dump(d, f)

with open('test.txt', 'rb') as f:
	print json.load(f)

json_str = '{"age":20, "score": 80, "name": "Jerry"}'
print json.loads(json_str)