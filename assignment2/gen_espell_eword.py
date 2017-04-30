f = open('eword-epron.data', 'r')
t = open('eword-espell.wfst', 'w+')
states = []
t.write('F\n')
for line in f:
    s = line.split()
    word = s[0]
    for idx in range(len(word)):
        if idx == 0:
            string = "(0 (" + word[idx] + " " + word[idx] + " *e* 1.0))" + '\n'
        elif idx < len(word):
            string = "(" + word[:idx] + " (" + word[:idx+1] + " " + word[idx] + " *e* 1.0))" + '\n'
        if string not in states:
            t.write(string)
            states.append(string)
    string = "(" + word + " (F *e* " + word + " 1.0))" + '\n'
    t.write(string)
t.close()
