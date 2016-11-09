#! /usr/bin/env python
#! -*- coding:utf-8 -*-

L = []
s = raw_input('Please input your name: ')
while len(s) is not 0:
	L.append(s)
	s = raw_input('Please input your name: ')

print map(str.capitalize, L)