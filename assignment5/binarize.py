# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 11:32:56 2017

@author: adivt
"""

from collections import defaultdict
import re

tree = open('pp.txt', 'r')
nonbinary = []
treedict = defaultdict(list)
leveldict = defaultdict(int)
rawinput = []
for line in tree:
    rawinput.append(line)

for line in range(len(rawinput)):
    currentLevel = rawinput[line].count('|')  #get current level
    leveldict[currentLevel] += 1
    for a in range(line+1, len(rawinput)):
        if rawinput[a].count('|') == currentLevel + 1:
            treedict[rawinput[line]].append(rawinput[a])
        elif rawinput[a].count('|') == currentLevel:
            print("i[a]=",rawinput[a],"   | appending [] to", rawinput[line])
            treedict[rawinput[line]].append([])
            break
        
for i in treedict.values():
    if len(i) > 1 and [] in i:
        i.remove([])
        
