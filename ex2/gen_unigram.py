from collections import defaultdict
f = open('realtrain.txt', 'r')

cntdict = defaultdict(dict)
ttlen = 0


for line in f:
    line = line.replace('\n', '</s>')
    #print line
    s = line.split()
    ttlen += len(s) 
    for i in range(0, len(s)):
	c = s[i]
	if c not in cntdict:
	    cntdict[c] = 1
	else:
	    cntdict[c] += 1
f.close()

state = list(cntdict.keys())

print 'F'
print '(0 (1 <s>))'
for j in state:
    #print cntdict[j], ttlen
    probs = round(cntdict[j]/float(ttlen), 5)
    if j != '</s>':
	print '(1 (1 '+j+' ' + str(probs)+ '))'   
    else:
	print '(1 (F '+j+' ' + str(probs)+ '))'
