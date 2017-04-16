"""
ASSIGNMENT 1
"""
states = []
f = open('vocab.small') #change to vocab for full dictionary
t = open('english.fsa', 'w+')   #create fsa file
#iterate thru every word in dict
for w in f:

    #iterate thru letter in word
    for l in range(0, len(w)+1):
        substr = w[:l]          #create substring
        substr = substr[:-2]    #remove trailing whitespace and \n
        #print (l, substr)

        #do duplicate checking, handle base cases of empty/space string
        if (substr not in states) and (substr != '') and (substr[-1] != ' '):

            #build state string that can be written to the fsa
            currentState = '(' + substr[:-1] + ' (' + substr + ', ' + substr[-1] + '))'
            #print currentState
            states.append(substr)

            t.write(currentState+'\n')

t.close()
