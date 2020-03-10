#!/usr/bin/python
import sys

lst = []
for line in sys.stdin:
	line = line.strip()
	lst = line.split('\t')

	if (lst[1]=="India"):
		print "%s\t%s" %(lst[0],lst[1])
