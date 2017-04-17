"""
ASSIGNMENT 1
"""
import sys

states = []
#f = open('vocab.small') #used for testing purposes
t = open('english.fsa', 'w+')   #create fsa file
#iterate thru every word in dict
t.write ('1\n')
for w in sys.stdin:

    #iterate thru letter in word
    for l in range(0, len(w)+1):
        substr = w[:l]          #create substring
        substr = substr[:-2]    #remove trailing whitespace and \n
        substr = substr.replace(" ", "")

        #do duplicate checking, handle base cases of empty/space string
        if (substr not in states) and (substr != '') and (substr[-1] != ' '):

            #build state string that can be written to the fsa
            currentState = '(' + substr[:-1] + ' (' + substr + ' ' + substr[-1] + '))'
            #print currentState
            states.append(substr)
            if '( (' in currentState:
                #print currentState
		currentState = currentState.replace('( (', '(0 (')
		#print currentState
            t.write(currentState+'\n')

    t.write('(' + substr + ' (1 *e*))\n')
t.write('(1 (0 _))\n')
t.close()
