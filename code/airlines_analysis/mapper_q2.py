import sys
lst = []
for line in sys.stdin:
    line = line.strip()
    lst = line.split(',')
    stop = int(lst[7])
    if stop == 0 :
        print "%s \t %d" %(lst[0],stop)
