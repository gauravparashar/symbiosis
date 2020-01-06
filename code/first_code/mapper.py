#/usr/bin/python
import sys
for line in sys.stdin:
    line =  line.strip() # Remove the leading and trailing spaces
    words =  line.split() # Split the line on space
    for word in words:
#         print "%s\t%s" %(word,1)
	 print '{0}\t{1}'.format(word, 1)
