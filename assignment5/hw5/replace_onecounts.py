#!/usr/bin/env python

import sys,re
from tree import *
from collections import defaultdict

list = sys.stdin.readlines()
dictionary_times = defaultdict(lambda:int(1))
dictionary_pos	 = defaultdict(lambda:int(0))

def find_terminal(tree,a):
	if tree.is_terminal():
		a.append(tree.word)
	else:
		for sub in tree.subs:
			find_terminal(sub,a)

def find_terminal_change(tree,word1):
	if tree.is_terminal():
		if tree.word == word1:
			tree.word = '<unk>'
	else:
		for sub in tree.subs:
			find_terminal_change(sub,word1)

line_num=0
for line in list:
	t = Tree.parse(line.strip())
	a = []
	find_terminal(t,a)
	# data = re.findall(r"([a-z]+)", line)
	for word in a:
	 	dictionary_times[word]+=1
	 	dictionary_pos[word]=line_num
	line_num+=1

for word in dictionary_times:
	if dictionary_times[word]==2:
		line_num = dictionary_pos[word]

		t = Tree.parse(list[line_num].strip())
		find_terminal_change(t,word)
		list[line_num] = str(t)#writeback
		# strinfo = re.compile(word)
		# list[line_num] = strinfo.sub('<unk>',list[line_num])
	else:
		sys.stderr.write(word+'\n')

for line in list:
	if line[-1] != '\n':
 		sys.stdout.write(line+'\n')
 	else:
 		sys.stdout.write(line)
