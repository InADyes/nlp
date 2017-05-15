import numpy as np
import re

"""
Weight matrix:
"""


def getWeights():
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
            tag_1_index = tags.index(x[0])
            tag_2_index = tags.index(x[1])
            if int(x[-1]) < 10:
                T[tag_1_index][tag_2_index] = int(x[-1])/10
            else:
                T[tag_1_index][tag_2_index] = int(x[-1])/100
        elif len(x) > 1 and x[1] in tags:
            tag_2_index = tags.index(x[1])
            E[tag_2_index] = int(x[-2])
    return (E,T)



def viterbi(line, E, T, tags):
    words = line.split()
    x = np.ones((len(tags), len(line)))
    
    for i, word in enumerate(words):
        if i == 0:
            for tagid, atag in enumerate(tags):
                x[tagid][i] = E.get((atag,aword.lower()),-1*np.inf)
                b[tagid][i] = -1 # Means this is the first word
            continue
        for atagid, atag in enumerate(tags):
            emmval = E.get((atag,aword.lower()),-1*1e10)
            for atagid_prev, atag_prev in enumerate(tags):
                trval = T.get((atag_prev,atag),-1*1e10)
                total = x[atagid_prev][i-1]+emmval+trval
                if total > x[atagid][i]:
                    x[atagid][i] = total
                    b[atagid][i] = atagid_prev
    idx = np.argmax(x[:][-1])
    annotate = []
    for idx_ in np.size(b,axis=1),0,-1):
        annotate.append(tags[int(idx)])
        idx = b[idx,idx_-1]
    annotate.reverse()
    return words,annot


tags = []
(E,T) = getWeights()