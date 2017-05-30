#!/usr/bin/python3
"""
ASSIGNMENT 4 NLP
@author: Aditya
"""

import re
from collections import defaultdict
from itertools import *
import sys

#file = open('epron-jpron.data','r')


epjp = []
inputStrings = []
iterations = int(sys.argv[1])


def isnumeric(string):
   return bool(re.search(r'\d', string))

def getAlignments(epron, jpron):
    
    #handle base case
    if len(epron) == 1:
        alignment = [[(''.join(epron), ''.join(jpron))]]
        return alignment
    
    #recursive case
    alignments = []
    for i in range(min(3, len(jpron), len(epron))):
        curr_j = ' '.join(jpron[:i + 1])
        align = getAlignments(epron[1:],jpron[i+1:])
        for r in align:
            alignments += [[(epron[0], curr_j)] + r]
    return alignments

#process input
for line in sys.stdin:
    line = line.split("\n")
    if not isnumeric(line[0]):
        inputStrings.append(line[0])
    #print(line)

for i in range(0, len(inputStrings)-2, 2): 
    estring = inputStrings[i]
    jstring = inputStrings[i+1]

    epron = estring.split()
    jpron = jstring.split()
    #print(epron, jpron)
    epjp.append((epron, jpron))



alignments = []
counts = defaultdict(lambda: defaultdict(float))
pr_prior = defaultdict(lambda: defaultdict(float))

#iterate thru every pairing to generate alignments
for pair in epjp:
    epron = pair[0]
    jpron = pair[1]
    al = getAlignments(epron, jpron)
   
    for a in al:
        for tpair in a:
            
            #only enumerate legal alignments
            #eliminates alignments like ("ER", "")
            #where epron does not map to any jpron
            if '' not in tpair:  
                counts[tpair[0]][tpair[1]] += 1
       
#initialize the probabilities               
for epron in counts.keys():
    for jpron in counts[epron].keys():
        count = sum([i for i in counts[epron].values()])
        pr_prior[epron][jpron] = counts[epron][jpron] / count
             

nonzero = 0
for epron in pr_prior.keys():
    for jpron in pr_prior[epron].keys():
        p_EJ = round(pr_prior[epron][jpron], 3)
        if p_EJ > 0.01:
            nonzero += 1
        #print(epron, " : ", jpron, " # ", p_EJ)

for i in range(iterations):

    p = 0
    total = 0
    probdict =  defaultdict(lambda: defaultdict(float))
    
    for pair in epjp:
        epron = pair[0]
        jpron = pair[1]
        alignments = getAlignments(epron, jpron)
        #print("alignments = ", len(alignments))
        tarray = []
        for a in alignments:
            p_accum = 1
            
            for tpair in a:
                p_accum *= pr_prior[tpair[0]][tpair[1]]
            
            tarray.append(p_accum)
            #print(tarray)
            total += p_accum
        asum = 0
        #print(tarray)
        for p in tarray:
            asum += p
        for p in tarray:
            if asum > 0:
                tarray = [p / sum(tarray) for p in tarray]
        #print(tarray)
        
        if not isinstance(tarray, list):
            tarray = [tarray]
        for x, j in enumerate(alignments):
           # print(tarray)
            for k in j:
                probdict[k[0]][k[1]] += tarray[x]

        print("iteration ",i," ----- corpus prob= ",total)
        for epron in pr_prior.keys():
            for jpron in pr_prior[epron].keys():
                p_EJ = round(pr_prior[epron][jpron], 3)
                if p_EJ > 0.01:
                    nonzero += 1
                    print(epron, " : ", jpron, " # ", p_EJ)
        
        print("Nonzero = ", nonzero)
        nonzero = 0
        for t in probdict.keys():
            q = 0
            for e in probdict[t].keys():
                q += probdict[t][e]
    
            for e in probdict[t].keys():
                if q > 0:
                    probdict[t][e] = probdict[t][e] / q
        pr_prior = probdict