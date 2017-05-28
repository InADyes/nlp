# -*- coding: utf-8 -*-
"""
Created on Sun May 28 10:53:10 2017

@author: adivt
"""
from collections import defaultdict
from itertools import *
import re

english_counts = {}
file = 'f'
x = {}
eprons = []
jprons = []
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

    
#    for i in range(len(jpron)):
#        if i < len(jpron) and jpron[i] == ' ' and mapping[i-1] == mapping[i+1]:
#            jpron[i] = '_'
    
    epron = ''.join(str(e) for e in epron)
    jpron = ''.join(str(e) for e in jpron)
    mapping = ''.join(str(e) for e in mapping)
    
    jphone = jpron.split()
    ephone = epron.split()
    eprons.append(ephone)
    jprons.append(jphone)
    
file.close()
forward = []
forward.append([1])
for word in range(eprons):
    forward[0][0] = 1
    n, m = len(eprons[word]), len(jprons[word])
    for i in range(0,n):
        for j in forward[i]:
            for k in range(1, min(m-j, 3)+1):
                jseg= tuple(jprons[j:j+k])
                score = forward[i][j] * 1
                
