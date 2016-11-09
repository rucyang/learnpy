#! /usr/bin/env python
#! -*- coding:utf-8 -*-

def calc_num(*args):
	ax = 0
	for i in args:
		ax = ax + i 
	return ax

def lazy_sum(*args):
	def sum():
		ax = 0
		for i in args:
			ax = ax + i
		return ax
	return sum

f1 = lazy_sum(1,2,3,4,6)
f2 = lazy_sum(1,2,3,4,6)

print f1 == f2

print '#######################################'

def count():
	fs = []
	for i in range(1,4):
		def f():
			return i * i
		fs.append(f)
	return fs

f3,f4,f5 = count()

print f3(), f4(), f5()

print "#######################################"
def count1():
	fs = []
	for i in range(1,4):
		def f(j):
			def g():
				return j * j
			return g
		fs.append(f(i))
	return fs

f6,f7,f8 = count1()

print f6(),f7(),f8()
			