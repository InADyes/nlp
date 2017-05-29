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

probs = defaultdict(lambda: defaultdict(float))
epjp = []

def getAlignments(epron, jpron):
    
    #handle base case
    if len(epron) == 1:
        alignment = [[''.join(epron), ''.join(jpron)]]
        return alignment
    
    alignments = []
    for i in range(min(3, len(jpron), len(epron))):
        curr_j = ' '.join(jpron[:i + 1])
        align = getAlignments(epron[1:],jpron[i+1:])
        alignments += [[(epron[0], curr_j)] + r for r in align]
    return alignments
        

while True:
    lines = islice(file, 3)

    stack =[]
    #create the stack
    for line in lines:
        stack.append(line)
    if stack == []:break
    epron = stack[0].split()#re.split(r'(\s+)', stack[0])
    jpron = stack[1].split()# re.split(r'(\s+)', stack[1])
    
    
    epjp.append((epron, jpron))
    
for pair in epjp:
    epron = pair[0]
    jpron = pair[1]
    al = getAlignments(epron, jpron)
    print (al)
    for a in al:
        print(a)
        for pair in a:
            x = 1
            del x
            #probs[pair[0]][pair[1]] += 1
    

    