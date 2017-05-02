f = open ('epron-jpron.probs', 'r')
t = open ('epron-jpron.wfst', 'w+')
t.write('F\n')
for line in f:
    s = line.split()
    if len(s) == 5:
	string = "(0 (0 " + s[0] + " " + s[2] + " " + s[4] + "))" + '\n'
	t.write(string)
    if len(s) == 6:
	string1 = "(0 (" + s[2] + "-" + s[3] + " " + s[0] + " " + s[2] + " " + s[5] + "))" + '\n'
	string2 = "(" + s[2] + "-" + s[3] + " (0 *e* " + s[3] + " 1.0))" + '\n'
	t.write(string1)
	t.write(string2)
    if len(s) == 7:
	stringa = "(0 (" + s[2] + "-" + s[3] + "-" + s[4] + "1 " + s[0] + " " + s[2] + " " + s[6] + "))" + '\n'
	stringb = "(" + s[2] + "-" + s[3] + "-" + s[4] + "1 (" + s[2] + "-" + s[3] + "-" + s[4] + "2 *e* " +s[3] + " 1.0))" + '\n'
	stringc = "(" + s[2] + "-" + s[3] + "-" + s[4] + "2 (0 *e* " + s[4] + " 1.0))" + '\n'
	t.write(stringa)
	t.write(stringb)
	t.write(stringc)
string = "(0 (F *e* *e* 1.0))"
t.write(string)
t.close()
f.close()
