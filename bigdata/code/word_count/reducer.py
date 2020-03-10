import sys
w2c={}

for line in sys.stdin:
    line=line.strip()
    word,count=line.split('\t')
    try:
        count=int(count)
    except ValueError:
        continue

    try:
        w2c[word]=w2c[word]+count
    except:
        w2c[word]=count

for word in w2c.keys():
    print"%s\t%s" %(word,w2c[word])
