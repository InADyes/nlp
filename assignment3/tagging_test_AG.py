import numpy as np
from collections import defaultdict
import re

"""
Weight matrix:
"""
def getprobabilities():
    wt = defaultdict(float)
    regex = re.compile('[^a-zA-Z0-9]')
    
    lexicon = open('lexicon-w-t.txt', 'r')
    for line in lexicon:
        x = regex.sub(' ', line)
        x = x.split()
        if len(x) < 1:
            return wt
        ptuple = (x[1], x[0])
        if len(x[-1]) > 1:
            wt[ptuple] = int(x[-1])/100
        else:
            wt[ptuple] = int(x[-1])/10
    return wt
        
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
        for tag in range(len(tags)):
            for tag_prev in range(len(tags)):
                ptt = T[tag_prev][tag]
                ptuple = (line[i], tags[tag])
                ptw = wt[ptuple]
                p = ptt * ptw
                mu = opt[i-1] * p
                #print(mu, i, p)
                if mu > opt[i]:
                    opt[i] = mu
                    back.append(tag)
    tag_seq = [0]* len(line)
    tag_seq[-1] = "***"
    for i in range(len(line), 0, -1):
        #print(back)
        tag_seq[i-1] = tags[back[i]]
    return tag_seq




tags = []

(E,T, tags) = getWeights(tags)
wt = getprobabilities()
line = "They can fish"#"The panda eats shoots and leaves"
results = viterbi(line, wt, T, tags)
print(results)