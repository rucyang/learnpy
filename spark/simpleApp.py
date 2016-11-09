#! /usr/bin/env python
#! -*- coding:utf-8 -*-

from pyspark import SparkContext

logFile = "D:\spark-2.0.0-bin-hadoop2.7\README.md"
sc = SparkContext("local","Simple App")
logData = sc.textFile(logFile).cache()

numAs = logData.filter(lambda s: "a" in s).count()
numBs = logData.filter(lambda s: "b" in s).count()

print "Lines with a: %i, lines withb: %i" % (numAs, numBs)