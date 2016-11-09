#! /usr/bin/env python
#! -*- coding:utf-8 -*-

class Student(object):
	"""docstring for Student"""
	
	@property
	def score(self):
		return self._score

	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be a integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0~100!')
		self._score = value

if __name__ == '__main__':
	s = Student()
	s.score = 100
	print s.score
