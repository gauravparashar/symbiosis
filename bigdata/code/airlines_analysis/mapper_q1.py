import sys

lst = []
for line in sys.stdin:
	line = line.strip()
	lst = line.split(',')
	print "%s\t%s" %(lst[0],lst[3])
    	#if lst[3] == 'India':
    		#print "%s"%(lst[0]) # Airport ID = lst[0], Name=lst[1], City=lst[2],Country=lst[3]


