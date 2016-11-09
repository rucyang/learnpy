#! /usr/bin/env python3
#!-*- coding:utf-8 -*-

import sys
from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("WordCount").setMaster("local")
sc = SparkContext(conf = conf)

inputFile = sys.argv[1]

lines = sc.textFile(inputFile)

words = lines.flatMap(lambda line: line.split())

wordcount = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b: a+b)

wordcount.saveAsTextFile("wordcount")

total_word = wordcount.map(lambda wordTuple: wordTuple[1]).reduce(lambda a,b: a+b)

print("单词总数：", total_word)

