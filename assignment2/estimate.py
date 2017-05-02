# -*- coding: utf-8 -*-
"""
CS519 NLP ASSIGNMENT 2
PART 3
"""
from collections import defaultdict
from itertools import *
import re

english_counts = {}
file = 'f'
x = {}
file = open('epron-jpron.data', 'r')
while True:
    lines = islice(file, 3)

    stack =[]
    #create the stack
    for line in lines:
        stack.append(line)
    if stack == []:break
    epron = re.split(r'(\s+)', stack[0])
    jpron = re.split(r'(\s+)', stack[1])
    mapping = re.split(r'(\s+)', stack[2])
    
    for i in range(len(jpron)):
        if i < len(jpron) and jpron[i] == ' ' and mapping[i-1] == mapping[i+1]:
            jpron[i] = '_'
    
    epron = ''.join(str(e) for e in epron)
    jpron = ''.join(str(e) for e in jpron)
    mapping = ''.join(str(e) for e in mapping)
    
    jphone = jpron.split()
    ephone = epron.split()
    
    for i in range(len(ephone)):
        if ephone[i] not in english_counts:
            english_counts[ephone[i]] = 1
        else:
            english_counts[ephone[i]] += 1
        jphone[i] = jphone[i].replace('_', ' ')
        if (ephone[i], jphone[i]) not in x: 
            x[ephone[i], jphone[i]] = 1
        else:
            x[ephone[i], jphone[i]] += 1
    

file.close()

t = open('epron-jpron.probs', 'w')

for i in x:
    string = ''
    ecount = english_counts[i[0]]
    jcount = x[i]
    print(round(jcount/ecount, 2))
    string += i[0] + ' : ' + i[1] + ' # ' + str(round(jcount/ecount, 2)) + '\n'
    #if round(jcount/ecount, 2) > 0.01:
    t.write(string)
t.close()
