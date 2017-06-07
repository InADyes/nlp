import sys
from cky import *
parser = PCFGParser()
for line in sys.stdin:
    sent = line
    tree = parser.parse(sent.split())
    print tree

