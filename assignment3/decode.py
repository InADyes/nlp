#!/usr/bin/python

from collections import defaultdict
import sys,re

def carmel(inputs,dictionary_epron, dictionary_e_toj):
    def findbest(i,dictionary_result,track):
        if i in dictionary_result:
            return 

        if i >= 3: 
            maxrange = 4
        elif i <= 1:
            maxrange = 2
        else:
            maxrange = 3

        for k in range(1,maxrange):
            tmp = ""
            for s in range(k):
                pos = i-s-1
                tmp = new[pos]+ " " +  tmp

            for epron in dictionary_e_toj[tmp]:
                tmp_n= i-k
                if (i-k >0):
                    findbest(tmp_n,dictionary_result,track)
                for str1 in dictionary_result[i-k]:
                    e2, e1 = str1.split(" ")
                    str_tmp = e1+" "+epron             
                    if str_tmp in dictionary_result[i]:
                        tmp_result =  dictionary_result[i-k][str1]*dictionary_epron[str1][epron]*dictionary_e_toj[tmp][epron]
                        if tmp_result > dictionary_result[i][str_tmp]:
                            dictionary_result[i][str_tmp]= tmp_result
                            track[i][str_tmp]= str(tmp_n)+"_"+str1
                    else:
                        dictionary_result[i][str_tmp] = dictionary_result[i-k][str1]*dictionary_epron[str1][epron]*dictionary_e_toj[tmp][epron]
                        track[i][str_tmp]= str(tmp_n)+"_"+str1

    def trackback(i,track,pp):
        if i == 0:
            return " "
        n,s = track[i][pp].split("_")
        num = int (n)
        e1,e = pp.split(" ")
        if num == 0:
            return e
        if e == "</s>":
            return trackback(num,track,s)
        return trackback(num,track,s)+" "+e

    new= re.findall(r"[\w']+", inputs)
    new.append("</s>")

    len_strings = len(new) 
    
    dictionary_result   = defaultdict(lambda: defaultdict(lambda: float(0.))) # result
    track   = defaultdict(lambda: defaultdict(lambda: strings("")))
    s_t = "<s>"+" "+"<s>"
    dictionary_result[0][s_t]=1
    j_string = ""

    findbest(len_strings,dictionary_result,track)
    max_result = 0
    pos = ""
    for pp in dictionary_result[len_strings]:
        if dictionary_result[len_strings][pp] > max_result:
            max_result = dictionary_result[len_strings][pp]
            pos = pp 
    print trackback(len_strings,track,pos),"#",max_result
dictionary_epron = defaultdict(lambda: defaultdict(lambda: float(0.)))
dictionary_e_toj = defaultdict(lambda: defaultdict(lambda: float(0.)))

file_name = sys.argv[1]
file_name2 = sys.argv[2]
file = open(file_name,'r')
file2 = open(file_name2, 'r')
list = file.readlines()
file.close()

for line in list:
    strings = line.split(" ")
    dictionary_epron[strings[0]+" "+strings[1]][strings[3]] = float(strings[5])

list = file2.readlines()
dictionary_e_toj["</s> "]["</s>"] = 1
for line in list:
    strings = line.split(" ")
    tmp = ""
    for s in strings[2:len(strings)-3]:
        tmp = tmp + s + " "
    dictionary_e_toj[tmp][strings[0]]= float(strings[len(strings)-2] )

list = sys.stdin
for line in list:
    carmel(line,dictionary_epron,dictionary_e_toj)