#!/bin/python 
###################### second method ######################
import sys

total=0
l=0

#Sum input values 
for line in sys.stdin:
        total = total+ float(line.strip())
        l = l +1

average=total/l

print 'The Average of the Array is',average

