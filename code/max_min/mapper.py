import sys
for line in sys.stdin:
    line=line.strip() # removes the trailing and leading spaces
    w1,w2,w3 = line.split(',')
    print "%s\t%s" %(w1,w3)

