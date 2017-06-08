import re,sys
from tree import *	


from collections import defaultdict
dictionary = defaultdict(lambda:tuple())


def binarize(tree):
	if not tree.is_terminal():
		if len(tree.subs) <= 2:
			for i in range(len(tree.subs)):	
				binarize(tree.subs[i])
		else:
			new_subs = [i for i in tree.subs]
			if str(tree.label)[-1]=='\'':
				string = '('+tree.label+' '
			else:
				string = '('+tree.label+'\' '
			for i in range(len(tree.subs)):	
				if i == 0:
					binarize(tree.subs[i])
				else:
					string += str(tree.subs[i])+' '
			string = string[:-1]
			string += ')'
			# print string
			_,_,new_t = Tree._parse(string.strip(),0,0,False)
			binarize(new_t)
			tree.subs[1] = new_t
			# print new_t
			# print tree.subs
			while len(tree.subs) >2:
				tree.subs.pop()
			# print new_subs
			# print tree.subs

for i, line in enumerate(sys.stdin):
	t = Tree.parse(line.strip())
	binarize(t)
	print t
	# print t.pp()
	# for sub in t.subs:
	# 	print sub.subs

    