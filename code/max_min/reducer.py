import sys
# input comes from STDIN
lst_weight = []
lst_sno = []
sno1=1
snp2=0
for line in sys.stdin:
    line = line.strip()
    sno,weight = line.split("\t")
    weight=float(weight)
    lst_weight.append(weight)
    lst_sno.append(sno)

min=lst_weight[0]
max=lst_weight[0]

for i in range(1,len(lst_weight)):
    
    if lst_weight[i] < min:
        min = lst_weight[i]
        sno1 = lst_sno[i] 
     #   print(sno1)
    
    if lst_weight[i] > max:
        max = lst_weight[i]
        sno2 = lst_sno[i]
      #  print(sno2)
        
    #print("i=",i)

#print(lst_sno)
print('Min= ',min,sno1)
print('Max= ',max,sno2)
