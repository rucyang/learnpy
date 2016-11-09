#! /usr/bin/env python
#! -*- coding:utf-8 -*-

def reverse_cmp(x,y):
	if x > y:
		return -1
	if x < y:
		return 1
	return 0

def reverse_sort(L):
	return sorted(L, reverse_cmp)

L = [x for x in range(10)]

print reverse_sort(L)
