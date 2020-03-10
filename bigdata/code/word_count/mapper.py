import sys

def remove_punct(word):
    lst=[]
    str=''
    punct = [',','.',';']
    for a in word:
        if not a in punct:
            lst.append(a)
    
    str=str.join(lst)
    return (str)

for line in sys.stdin:
    line =  line.strip() # Remove the leading and trailing spaces
    words =  line.split() # Split the line on space
    for word in words:
         print "%s\t%s" %(remove_punct(word),1)
#        print(remove_punct(word))        
