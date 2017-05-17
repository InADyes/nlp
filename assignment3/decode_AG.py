import numpy as np
from collections import defaultdict
import re

def readfiles():
    epron_bigram = defaultdict(float)
    epronfile = open('epron.probs', 'r')
    for line in epronfile:
        x = re.split(r"[\#\:]", line)
        ptuple = (x[0], x[1])
        prob = x[2].rstrip('\n')
        epron_bigram[ptuple] = float(prob)
    epronfile.close()
    
    tfile = open('epron-jpron.probs', 'r')
    epron_jpron_probs = defaultdict(float)
    epron_jpron_mapping = defaultdict(list)
    for line in tfile:
        x = re.split(r"[\#\:]", line)
        epron_jpron_mapping[x[0]].append(x[1])
        ptuple = (x[0], x[1])
        prob = x[2].rstrip('\n')
        epron_jpron_probs[ptuple] = float(prob)
    return (epron_bigram, epron_jpron_probs, epron_jpron_mapping)

def viterbi(line, epron_bigram_probs, epron_jpron_probs, epron_jpron_mapping):
    line =  line.split()
    opt = [0]*len(line)
    back = []
    opt[0] = 1
    
    for i in range(len(line)):
        for phon in epron_jpron_mapping[line[i]]:
            for phon_prev in epron_jpron_mapping[line[i-1]]:
                for phon_pp in epron_jpron_mapping[line[i-2]]:
                    p_w = 
    
(epron_bigram_probs, epron_jpron_probs, epron_jpron_mapping) = readfiles()