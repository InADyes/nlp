from collections import defaultdict

f = open('train.trees.space','r')
cntdict = defaultdict(dict)

for line in f:
    s = line.split()
    for i in range(0, len(s)):
	#print s[i]
	if s[i] not in cntdict:
	    cntdict[s[i]] = 1
	else:
	    cntdict[s[i]] += 1
f.close()
f = open('train.trees.space','r')
for lines in f:
    k = lines.split() 
    for n,i in enumerate(k):
	if cntdict[i] == 1:
	    k[n] = '<unk>'
	    #lines.replace(old,'<unk>')
	    #print k[b]
    str1 = ''.join(k)
    #print str1
f.close()

words = list(cntdict.keys())
for p in words:
    if cntdict[p] > 1 and p != '(' and p != ')' and p != '_':
	print p 
