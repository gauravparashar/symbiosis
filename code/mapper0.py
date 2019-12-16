import sys
for line in sys.stdin:
    line=line.strip() # removes the trailing and leading spaces
    words = line.split()
    for word in words:
        print"%s\t%s" %(word,1)
