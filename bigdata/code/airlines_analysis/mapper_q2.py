#!/usr/bin/python
#Find the list of Airlines having zero stops
import sys
lst = []
for line in sys.stdin:
	line = line.strip()
    	lst = line.split(',')
	print "%s\t%s" %(lst[1],lst[7])
