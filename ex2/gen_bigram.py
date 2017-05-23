# -*- coding: utf-8 -*-
from collections import defaultdict
f = open('realtrain.txt', 'r')

cntdict1 = defaultdict(dict)
cntdict2 = defaultdict(dict)
ttlen = 0


chars = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(len(chars)):
    for j in range(len(chars)):
	bistate = chars[i]+chars[j]
	if bistate not in cntdict2:
	    cntdict2[bistate] = 1



for line in f:
    line = line.replace('\n', '</s>')
    #print line
    s = line.split()
    ttlen += len(s) 
    for i in range(0, len(s)):
        c = s[i]
	if c not in cntdict1:
	    cntdict1[c] = 1
	else:
	    cntdict1[c] += 1
    for i in range(0, len(s)-1):
	 c = s[i]+s[i+1]	   
	 if c not in cntdict2:
	    cntdict2[c] = 1
	 else:
	    cntdict2[c] += 1
f.close()

state1 = list(cntdict1.keys())
state2 = list(cntdict2.keys())


print 'F'
print '(0 (1 <s>))'
for j in state1:
    #print cntdict[j], ttlen
    cntdict1[j] = cntdict1[j]/float(ttlen)
    probs = cntdict1[j]
    if j != '</s>':
	print '(1 (' + j +' '+ j + ' ' + str(probs) + '))'
    else:
	print '(1 (F '+j+' ' + str(probs)+ '))'

    #print cntdict1[j]
for k in state2:    
    cntdict2[k] = cntdict2[k]/float(ttlen-1)

for j in state1:
    for k in state2:
	if j == k[0]:
	    probs = cntdict2[k]/cntdict1[j]
	    if k[1] != '<':	        
	        print '('+j+' ('+k[1]+' '+k[1]+' '+str(probs)+'))'
	    else:
		print '('+j+' (F </s> '+str(probs)+'))'


	
