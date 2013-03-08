#!/bin/python 
###################### second method ######################
import sys

total=0
l=0
filename='data.txt'
#Sum input values 
for line in filename:
        total = total+ float(line.strip())
        l = l +1

average=total/l

print 'The Average of the Array is',average
# You have a good boyfriend! 
