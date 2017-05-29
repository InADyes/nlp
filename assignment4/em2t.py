from collections import defaultdict
epron = ['AE', 'K', 'T']
jpron = ['A','K','U','T','O']

ejpairs = defaultdict(list)
ejpairs['AE'] = ['A','A K']
ejpairs['K'] = ['K','K U']
ejpairs['T'] = ['U T', 'T', 'T O']

pairsprob = defaultdict(dict)
pairsprob['AE-A'] = 1/7.0
pairsprob['AE-A K'] = 1/7.0
pairsprob['K-K'] = 1/7.0
pairsprob['K-K U'] = 1/7.0
pairsprob['T-T'] = 1/7.0
pairsprob['T-U T'] = 1/7.0
pairsprob['T-T O'] = 1/7.0

forward[][] = []
forward[0][0] = 1
l = 0

n, m = len(epron), len(jpron)
for i in xrange(0, n):
    ep = epron[l]
    for j in epairs[ep]:
	for k in range(0, len(ejpairs[ep]):
	    jseg = ejpairs[ep][k]
	    ejseq = ep+'-'+ejpairs[ep][k]
	    score = forward[i][j]*pairsprob[ejseq]
	    forward[i+1][j+k] += score


      	
    		 
