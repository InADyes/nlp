import re,sys
from tree import *	
from collections import defaultdict
dictionary = defaultdict(lambda:defaultdict(lambda:float(0.)))
# dictionary1 = defaultdict()
# file = open('train.dict','r')
# file_1 = file.readlines()
# for line in file_1:
# 	dictionary1[line[:-1]]=1
# # print dictionary1
def learn(tree):
	LHS = tree.label
	if not tree.is_terminal():
		_RHS = [i.label for i in tree.subs]
		_string =''
		for i in _RHS:
			_string += i +' '
		_string = _string[:-1]
		dictionary[LHS][_string]+=1
		for i in tree.subs:
			learn(i)
	else:
		RHS = tree.word
		dictionary[LHS][RHS]+=1

for i, line in enumerate(sys.stdin):
	t = Tree.parse(line.strip())
	learn(t)

for LHS in dictionary:
	tmp_sum = 0.
	for RHS in dictionary[LHS]:
		tmp_sum += dictionary[LHS][RHS]
	for RHS in dictionary[LHS]:
		dictionary[LHS][RHS]=dictionary[LHS][RHS]/tmp_sum
# count_2 = 0
# count_1 = 0
# count_end = 0
print 'TOP'
for RHS in dictionary['TOP']:
	print 'TOP -> '+RHS+' # '+str(dictionary['TOP'][RHS])
	# if len(RHS.split(' '))==2:
	# 	count_2 +=1
	# else:
	# 	count_1 +=1
for LHS in dictionary:
	if LHS != 'TOP':
		for RHS in dictionary[LHS]:
			print LHS+' -> '+RHS+' # '+str(dictionary[LHS][RHS])
# 			if RHS in dictionary1:
# 				count_end +=1
# 				continue
# 			if len(RHS.split(' '))==2:
# 				count_2 +=1
# 			else:
# 				count_1 +=1
# print count_2,count_1,count_end