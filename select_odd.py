#! /usr/bin/env python
#! -*- coding:utf-8 -*-

def is_odd(n):
	return n % 2 == 1

def not_empty(s):
	return s and s.strip()

L = [x for x in range(100) if x > 0]

print filter(is_odd, L)
print filter(not_empty, ["jerry",'','Tom'])