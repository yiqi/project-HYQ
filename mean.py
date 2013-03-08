#!/bin/python 
###################### second method ######################
import sys

total=0
l=0

#Sum input values 
for line in ('data_2.txt'):
        total = total+ float(line.strip())
        l = l +1

average=total/l

print 'The Average of the Array is',average
# You have a good boyfriend! 
