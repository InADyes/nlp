from collections import defaultdict
print '1'
f = open('strings')
line = f.readline()
line = line.replace('\n', '_')

cntdict = defaultdict(dict)
cntdict['0'] = defaultdict(dict)

while line:
    s = ''
    for c in line:
        if c.isspace():
            continue
        if s=='':
            if c not in cntdict['0']:
                cntdict['0'][c]=1
            else:
                cntdict['0'][c] += 1
        else:
            if s not in cntdict:
                cntdict[s] = defaultdict(dict)
            if c not in cntdict[s]:
                cntdict[s][c] =1
            else:
                cntdict[s][c] += 1
        if c == '_':
            s = ''
        else:
            s+=c
    line = f.readline()
    line = line.replace('\n', '_')
f.close()

states = list(cntdict.keys())
states.sort()

for s in states:
    ctot = 0
    trans=cntdict[s].keys()
    trans.sort()
    for c in trans:
        ctot += cntdict[s][c]
    for c in trans:
        prob = round((cntdict[s][c]/float(ctot)),3)
        #print (prob,cntdict[s][c], ctot)
        if c == '_':
            #print " "
            print '(' +s+' (1 *e* '+str(float(prob))+'))'
        else:
            if s == '0':
                #print " "
                print '(' +s+' ('+c+' '+c+' '+str(float(prob))+'))'
            else:
                #print " "
                print '(' +s+' ('+s+' '+c+' '+c+' '+str(float(prob))+'))'
print'(1 (0 _ 1.0))'
