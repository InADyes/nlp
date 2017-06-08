import re
from collections import defaultdict
import sys
from tree import *

def unaryCheck(dict,node_dict):
    list=[]
    for RHS in node_dict:
        if RHS in dict:
            for LHS in dict[RHS]:
                prob = node_dict[RHS][0] * dict[RHS][LHS]
                string = '('+LHS+' '+node_dict[RHS][1]+')'
                list.append((LHS,prob,string))

    while(len(list)>0):
        UNARY,PROB,STRING = list.pop(0)
        if (UNARY not in node_dict) or (PROB > node_dict[UNARY][0]):
            # node_dict[UNARY][0]= PROB
            # node_dict[UNARY][1] = STRING
            node_dict[UNARY] = (PROB, STRING)
            # LHS -> UNARY
            for LHS in dict[UNARY]:
                prob = node_dict[UNARY][0] * dict[UNARY][LHS]
                string = '('+LHS+' '+node_dict[UNARY][1]+')'
                list.append((LHS,prob,string))
    # print 1

def foo1(dict,SENTENCE,_words = []):

    # sentence = "I need to arrive early today"
    #
    # sentence = sentence.split()

    sentence = SENTENCE.split()

    LENGTH = len(sentence)

    tot_dict = defaultdict(lambda:defaultdict(lambda:defaultdict(lambda:(float(0.),""))))

    for span in xrange(LENGTH):
        for i in xrange(LENGTH-span):
            if span == 0:
                if sentence[i] in dict or sentence[i] in _words:
                    RHS = sentence[i]
                    for LHS in dict[RHS]:
                        # tot_dict[i][i][LHS][0]= dict[RHS][LHS]
                        # tot_dict[i][i][LHS][1]='('+LHS+' '+RHS+')'
                        prob = dict[RHS][LHS]
                        string = '('+LHS+' '+RHS+')'
                        tot_dict[i][i][LHS] = (prob,string)
                else:
                    RHS='<unk>'
                    for LHS in dict[RHS]:
                        # tot_dict[i][i][LHS][0] = dict[RHS][LHS]
                        # tot_dict[i][i][LHS][1] = '('+LHS+' '+sentence[i]+')'
                        prob = dict[RHS][LHS]
                        string = '('+LHS+' '+sentence[i]+')'
                        tot_dict[i][i][LHS] = (prob,string)
                unaryCheck(dict,tot_dict[i][i])

            else:
                j=i+span
                for k in xrange(i,j):
                    for left in tot_dict[i][k]:

                        for right in tot_dict[k+1][j]:
                            RHS = left + ' ' + right
                            for LHS in dict[RHS]:
                                prob = tot_dict[i][k][left][0] * tot_dict[k + 1][j][right][0] * dict[RHS][LHS]#change
                                SUBL = tot_dict[i][k][left][1]
                                SUBR = tot_dict[k + 1][j][right][1]
                                if (LHS not in tot_dict[i][j]) or (prob > tot_dict[i][j][LHS][0]):
                                    # tot_dict[i][j][LHS][0]= tot_dict[i][k][0] * tot_dict[k+1][j][0]

                                    # tot_dict[i][j][LHS][1]= '('+LHS+' '+SUBL +' ' +SUBR + ')'
                                    string = '('+LHS+' '+SUBL +' ' +SUBR + ')'
                                    tot_dict[i][j][LHS] = (prob,string)
                unaryCheck(dict, tot_dict[i][j])

    return tot_dict[0][LENGTH-1]["TOP"][1]

def debinarize(tree):#lexion
    if tree.is_terminal():
        return 
    if len(tree.subs) == 1:#unaray 
        debinarize(tree.subs[0])
    else:#binary
        #left son 
        debinarize(tree.subs[0])
        #right son
        debinarize(tree.subs[1])
        if tree.subs[1].label[-1] == '\'': #is can debinary one 
            tmp = [i for i in tree.subs[1].subs]
            tree.subs[1] = tmp[0]
            for i in xrange(1,len(tmp)):
                tree.subs.append(tmp[i])
            

if __name__ == "__main__":
    if len(sys.argv) > 1:

        file = open(sys.argv[1],'r')
        LINES = file.readlines()
        file.close()

        dict = defaultdict(lambda:defaultdict(lambda:float()))
        #the rules
        for LINE in LINES[1:]:
            line = re.split('->|#',LINE)
            LHS = line[0].strip()
            Prob = line[2].strip()
            RHS = line[1].lstrip().rstrip()
            dict[RHS][LHS]=float(Prob)

        if len(sys.argv) == 2:
            #run 1
            LINES = sys.stdin.readlines()
            result = ["" for i in xrange(len(LINES))]
            line_num = 0
            for line in LINES:
                result[line_num]=foo1(dict,line)
                line_num+=1

            for sentence in result:
                t = Tree.parse(sentence)
                debinarize(t)
                print t
        elif len(sys.argv) == 3:
            #run 2
            LINES = sys.stdin.readlines()
            file_word = open(sys.argv[2],'r')
            words = file_word.readlines()
            _words = []
            for word in words:                
                _words.append(word[:-1])

            result = ["" for i in xrange(len(LINES))]
            line_num = 0
            for line in LINES:
                result[line_num]=foo1(dict,line,_words)
                line_num+=1

            for sentence in result:
                t = Tree.parse(sentence)
                debinarize(t)
                print t