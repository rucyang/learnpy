#! /usr/bin/env python
#! -*- coding:utf-8 -*-
import functools

def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print '%s %s()' % (text,func.__name__)
			return func(*args, **kw)
		return wrapper
	return decorator

@log('execute')
def now(s):
	print s

now("My name is Jerry")
print now.__name__

