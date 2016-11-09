#! /usr/bin/env python
#! -*- coding:utf-8 -*-

class Fib(object):
	"""docstring for Fib"""
	def __init__(self):
		self.a, self.b = 0, 1

	def __iter__(self):
		return self

	def next(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 10000:
			raise StopIteration()
		return self.a

	def __getitem__(self, n):
		if isinstance(n, int):
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a
		if isinstance(n, slice):
			start = n.start
			stop = n.stop
			step = n.step
			a, b = 1, 1
			L = []
			if start is None:
				start = 0
			for x in range(stop):
				if x >= start and (x - start)%step == 0:
					L.append(a)
				a, b = b, a + b
			return L

class Chain(object):
	"""docstring for Chain"""
	def __init__(self, path = 'https:/'):
		self._path = path

	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path, path))
	def __str__(self):
		return self._path
		
if __name__ == '__main__':
	f = Fib()
	print f[:1000:3]
	print Chain().www.baidu.com
	# for n in Fib():
	# 	print n

		
