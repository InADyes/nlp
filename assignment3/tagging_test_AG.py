import numpy as np
import re

"""
Weight matrix:
"""

tags = []

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
    file.close()
    file = open('bigram.wfsa', 'r')
    for line in file:
        x = regex.sub(' ', line)
        x = x.split()
        print(x)
        if x[0] in tags and x[1] in tags:
            tag_1_index = tags.index(x[0])
            tag_2_index = tags.index(x[1])
            if int(x[-1]) < 10:
                T[tag_1_index][tag_2_index] = int(x[-1])/10
            else:
                T[tag_1_index][tag_2_index] = int(x[-1])/100
        
    return T

T = getWeights()

def viterbi(str):
    T = len(str)
    