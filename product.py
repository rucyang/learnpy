#! /usr/bin/env python
#! -*- coding:utf-8 -*-

def prod(L):
	print reduce(lambda x, y : x * y, L)

L = [x for x in range(10)][1:]

prod(L)	