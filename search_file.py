#! /usr/bin/env python
#! -*- coding:utf-8 -*-

import os
import sys



def search(s):
	for dirpath, dirnames, filenames in os.walk('.'):
		for filename in filenames:
			if s in filename:
				print os.path.join(dirpath, filename)[2:]

if __name__ == "__main__":	
	search(sys.argv[1])