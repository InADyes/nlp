import numpy as np
from collections import defaultdict
import re

"""
Weight matrix:
"""
def getprobabilities():
    wt = defaultdict(float)
    regex = re.compile('[^a-zA-Z0-9]')
    tag_dict = defaultdict(list)
    lexicon = open('lexicon-w-t.txt', 'r')
    for line in lexicon:
        x = regex.sub(' ', line)
        x = x.split()
        #print(x)
        if len(x) < 1:
            return (wt, tag_dict)
        ptuple = (x[1], x[0])
        tag_dict[x[1]].append(x[0])
        if len(x[-1]) > 1:
            wt[ptuple] = int(x[-1])/100
        else:
            wt[ptuple] = int(x[-1])/10
    return (wt, tag_dict)
        
def getWeights(tags):
    file = open('bigram.wfsa', 'r')
    regex = re.compile('[^a-zA-Z0-9]')
    for line in file:
        x = regex.sub(' ', line)
        x = x.split()
        for i in x:
            if i.isalpha() and i not in tags and i != 'F' and i != 'e':
                tags.append(i)
    T = np.zeros((len(tags), len(tags)))
    E = np.zeros(len(tags))
    file.close()
    file = open('bigram.wfsa', 'r')
    for line in file:
        x = regex.sub(' ', line)
        x = x.split()
        #print(x)
        if x[0] in tags and x[1] in tags:
            tag_prev_index = tags.index(x[0])
            tag_curr_index = tags.index(x[1])
            if int(x[-1]) < 10:
                T[tag_prev_index][tag_curr_index] = int(x[-1])/10
            else:
                T[tag_prev_index][tag_curr_index] = int(x[-1])/100
        elif len(x) > 1 and x[1] in tags:
            tag_curr_index = tags.index(x[1])
            E[tag_curr_index] = int(x[-2])
    return (E,T, tags)

def viterbi(line, wt, T, tags):
    line = line.split()
    opt = [0]*len(line)
    back = []
    opt[0] = 1
    for i in range(len(line)):
        for tag in tag_dict[line[i]]:   #tag = tag of word i
            for tag_prev in tag_dict[line[i-1]]:    #t_prev = tag of i - 1
                                
                ###ERROR IS PROBABLY HERE####
                ptuple = (line[i], tag)
                #print(ptuple)
                ptt = T[tags.index(tag_prev)][tags.index(tag)] #ptt = p(tag | tag_prev)
                ptw = wt[ptuple] #ptw = p(word | tag)
                p = ptt * ptw #p = p(tag | tag_prev) * p(word | tag)
                mu = opt[i-1] * p #prob of best seq ending in i - 1
                
                if mu > opt[i]:
                    opt[i] = mu
                    back.append(tag)
                
                #############################
    
    del back[-1]             
    tag_seq = [0]* len(line)
    for i in range(len(line), 0, -1):

        tag_seq[i-1] = back[i-1]
    return tag_seq




tags = []

(E,T, tags) = getWeights(tags)
(wt, tag_dict) = getprobabilities()
line = "They can fish"#"The panda eats shoots and leaves"
results = viterbi(line, wt, T, tags)
print(results)