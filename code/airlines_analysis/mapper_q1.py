import sys

lst = []
for line in sys.stdin:
    line = line.strip()
    lst = line.split(',')
    if lst[3] == 'India':
        print "airport ID: %s \tName: %s\tCity: %s\tCountry: %s"    %(lst[0],lst[1],lst[2],lst[3]) # Airport ID = lst[0], Name=lst[1], City=lst[2],Country=lst[3]
    

