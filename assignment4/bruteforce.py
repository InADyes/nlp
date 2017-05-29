import random
from collections import defaultdict


EPJPdict = defaultdict(dict)
EJpair = ['W_W','AY_A','N_I-N','AY_A-I','N_N','W_W-A','AY_I']

for s in EJpair:
    if s not in EPJPdict:
	EPJPdict[s] =1/float(len(EJpair))
	#if len(s) == 3:
	#    print s[0] +'|->  '+s[2]+': '+str(EPJPdict[s])
	#if len(s) == 4:
	#    print s[:1] +'|->  '+s[3]+': '+str(EPJPdict[s])
	#if len(s) == 5:
	#    print s[0] +'|->  '+s[2]+' '+s[4]+': '+ str(EPJPdict[s])
	#if len(s) == 6:
	#    print s[:1] +'|->  '+s[3]+' '+s[5]+': '+str(EPJPdict[s])

#f = open('lined.txt', 'r')
#lines = f.readlines()
#f.close() 
#for i in range(0,len(lines)):
#    print lines[i]

#ejpairs = list(EPJPdict.keys())

FracPz1 = 0
FracPz2 = 0
FracPz3 = 0
corpusP = 0

for i in range (0,5):
    Pz1 = EPJPdict['W_W'] * EPJPdict['AY_A'] * EPJPdict['N_I-N']
    Pz2 = EPJPdict['W_W'] * EPJPdict['AY_A-I']* EPJPdict['N_N']
    Pz3 = EPJPdict['W_W-A'] * EPJPdict['AY_I'] * EPJPdict['N_N']
    FracPz1 = Pz1/(Pz1+Pz2+Pz3)
    FracPz2 = Pz2/(Pz1+Pz2+Pz3)
    FracPz3 = Pz3/(Pz1+Pz2+Pz3)
    corpusP = Pz1+Pz2+Pz3
    print 'iteration '+str(i)+' ----- corpus prob= '+str(corpusP)
    
    EPJPdict['W_W'] = (FracPz1+FracPz2)
    EPJPdict['AY_A'] = FracPz1
    EPJPdict['N_I-N'] = FracPz1
    EPJPdict['AY_A-I'] = FracPz2
    EPJPdict['N_N'] = FracPz2+FracPz3
    EPJPdict['W_W-A'] = FracPz3
    EPJPdict['AY_I'] = FracPz3
    #print 'AY|-> A: '+str(round(EPJPdict['AY_A'],2)) +' A I: '+str(round(EPJPdict['AY_A-I'],2))+ ' I: '+str(round(EPJPdict['AY_I],2))
    print 'W|->  W: '+str(round(EPJPdict['W_W'],2)) + ' W A: '+str(round(EPJPdict['W_W-A'],2))
    print 'N|->  N: '+str(round(EPJPdict['N_N'],2)) + ' I N: '+str(round(EPJPdict['N_I-N'],2))
    
#print 'Pz1: '+str(Pz1)
#print 'Pz2: '+str(Pz2)
#print 'Pz3: '+str(Pz3)
