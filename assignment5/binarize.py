# -*- coding: utf-8 -*-
"""
<<<<<<< HEAD
Created on Sat Jun  3 16:51:59 2017

@author: Aditya
"""
import sys


from tree import Tree
import gflags as flags
FLAGS=flags.FLAGS
flags.DEFINE_integer("max_len", 400, "maximum sentence length")
flags.DEFINE_boolean("pp", False, "pretty print(")
flags.DEFINE_boolean("height", False, "output the height of each tree")
flags.DEFINE_boolean("wordtags", False, "output word/tag sequence")
flags.DEFINE_boolean("words", False, "output word sequence")
flags.DEFINE_boolean("clean", False, "clean up functional tags and empty nodes")
    
argv = FLAGS(sys.argv)


f = open('train.trees.unk', 'r')
trees = []
line = "(TOP (SQ (VBZ Does) (NP (DT this) (NN flight)) (VP (VB serve) (NP (NN dinner)))))"

t = Tree.parse(line.strip()) #main tree parsing function
print(line)
print(t.pp()) #prints the tree as a visual tree
=======
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
        
>>>>>>> 221041072202d6a14e9e2f226391d03c9c44b352
