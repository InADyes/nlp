# -*- coding: utf-8 -*-
"""
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
