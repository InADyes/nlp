from tree import Tree
import sys
from collections import defaultdict

countdict = defaultdict(int)
probdict = defaultdict(lambda: defaultdict(int))


def getCounts(tree, countdict, probdict):

    #update tag counts, create dictionary
    countdict[tree.label] += 1
    if tree.label not in probdict:
        probdict[tree.label] = defaultdict(int)

    #if at leaf node, update prob for label -> word
    if tree.is_terminal():
        probdict[tree.label][tree.word] += 1
    else:
        #get left child
        updatedTag = tree.subs[0].label
        if len(tree.subs)>1:
            updatedTag += " " + tree.subs[1].label

        #update prob for label -> left child
        probdict[tree.label][updatedTag] += 1

        #recurse on left child
        getCounts(tree.subs[0], countdict, probdict)

        #if right child exists, recurse on right child
        if len(tree.subs) > 1:
            getCounts(tree.subs[1], countdict, probdict)
            
    return (probdict, countdict)

for line in sys.stdin:
    tree = Tree.parse(line)
    getCounts(tree, countdict, probdict)
    
#divide probdict counts by overall num tags to get probs
for i in probdict:
    for j in probdict[i]:
        probdict[i][j] /= float(countdict[i])
    
#print results
binary = 0
unary = 0
lexical = 0
print("TOP")
for i in probdict:
    for j in probdict[i]:
        if j in probdict.keys():
            unary += 1
        elif ' ' in j:
            binary += 1
        else:
            lexical += 1
        string = i + " -> " + j + " # " + str(probdict[i][j])
        print(string)
#print "Binary rules: ", binary, "\nUnary rules: ", unary, "\nLexical rules: ", lexical
