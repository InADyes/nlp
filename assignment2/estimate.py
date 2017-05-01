# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 14:52:31 2017

@author: adivt
"""
from collections import defaultdict
from itertools import *
file = 'f'
tuples = []
x = {}
stacks = []
#while file:
with open('epron-jpron-small.data', 'r') as file:
    lines = islice(file, 3)

    stack =[]
    
    #create the stack
    for line in lines:
        stack.append(line)
    
    epron = stack[0].split()
    jpron = stack[1].split()
    mapping = [int(i) for i in stack[2].split()]
    skip = False
    dup = ''
    tlist = []
    for i in range(len(mapping)):
        tlist.append([epron[mapping[i]-1], jpron[i]])
    
    for i in range(len(tlist)):
        if tlist[i][0] not in x: 
            x[tlist[i][0]] = []
    substr = ''
    ctr =0
    for i in range(len(tlist)):
        if i < (len(tlist)-1) and tlist[i][0] == tlist[i+1][0]:
            if ctr == 0:
                substr = ''
                substr += tlist[i][1]+ tlist[i+1][1]
            else:
                substr += tlist[i][1]
            ctr += 1
            print((tlist[i][0], tlist[i+1][0] ,  substr))
        else:
            substr = tlist[i][1]
            print((tlist[i][0],  substr))
            
        x[tlist[i][0]].append(substr)
        
#        for i in range(len(jpron)):
#            t=[epron[int(mapping[i])-1], jpron[i]]
#            tuples.append(t)
        
#        for i in tuples:
#            
#            #if the Key-Value pair does not exist, create a kvp of the following
#            #key = (epron, jpron)
#            #value = (count of jpron, count of epron)
#            #
#            if not x[i]:
#                x[i] = (1, 1)
#            else:
#                x[i] = 
                
                
            