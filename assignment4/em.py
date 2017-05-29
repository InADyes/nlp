# -*- coding: utf-8 -*-
"""
ASSIGNMENT 4 NLP
@author: Aditya
"""

import numpy as np
import re
from collections import defaultdict
from itertools import *

file = open('epron-jpron.data.test', 'r')

def isnumeric(string):
   return bool(re.search(r'\d', string))

counts = defaultdict(lambda: defaultdict(float))
probs = defaultdict(lambda: defaultdict(float))
epjp = []

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
while True:
    lines = islice(file, 3)

    stack =[]
    
    #create the stack
    for line in lines:
        stack.append(line)
    if stack == []:break
    epron = stack[0].split()
    jpron = stack[1].split()
    
    epjp.append((epron, jpron))

alignments = []

#iterate thru every pairing to generate alignments
for pair in epjp:
    epron = pair[0]
    jpron = pair[1]
    al = getAlignments(epron, jpron)
   
    for a in al:
        for pair in a:
            
            #only enumerate legal alignments
            #eliminates alignments like ("ER", "")
            #where epron does not map to any jpron
            if '' not in pair:  
                counts[pair[0]][pair[1]] += 1
                      
for epron in counts.keys():
    for jpron in counts[epron].keys():
        probs[epron][jpron] = counts[epron][jpron] / sum([i for i in counts[epron].values()])