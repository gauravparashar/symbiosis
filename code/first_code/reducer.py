import sys

w = {}

# Process each key-value pair from the mapper
for line in sys.stdin:
    # Get the key and value from the current line
    word, count = line.split('\t')
    # Convert the count to an int
    count = int(count)
    
    if word in w:
        w[word] = w[word] + count
    else:
        w[word] = count


for word in w.keys():
    print"%s\t%s" %(word,w[word])
