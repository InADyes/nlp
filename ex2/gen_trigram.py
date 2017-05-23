# -*- coding: utf-8 -*-
from collections import defaultdict
f = open('realtrain.txt', 'r')

cntdict1 = defaultdict(dict)
cntdict2 = defaultdict(dict)
cntdict3 = defaultdict(dict)
ttlen = 0


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
    for i in range(0, len(s)-2):
	c = s[i]+s[i+1]+s[i+2]
	if c not in cntdict3:
	    cntdict3[c] = 1
	else:
	    cntdict3[c] += 1
f.close()

state1 = list(cntdict1.keys())
state2 = list(cntdict2.keys())
state3 = list(cntdict3.keys())

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
	        print '('+j+' ('+k+' '+k[1]+' '+str(probs)+'))'
	    else:
		print '('+j+' (F </s> '+str(probs)+'))'

for l in state3:
    cntdict3[l] = cntdict3[l]/float(ttlen-2)
	
for k in state2:
    for l in state3:
	probs = cntdict3[l]/cntdict2[k]
	if k[0] == l[0] and k[1] == l[1]:
	    if l[2] != '<':
		print '('+l[:2]+' ('+l[1:]+' '+l[2]+' '+str(probs)+'))'
	    else:
		print '('+l[:2]+' (F </s> '+str(probs)+'))'
