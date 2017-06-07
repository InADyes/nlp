from cky import *
parser = PCFGParser()
sent = "I need a flight from Atlanta to Charlotte North Carolina next Monday"
tree = parser.parse(sent.split())
