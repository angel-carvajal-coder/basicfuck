from sys import argv
from util import *
from parser_ import parse
from collections import namedtuple

Variable = namedtuple('Variable', ['name', 'length'])

with open(argv[1], 'r') as f:
    lines = list(f)

# Parse first directive
firstDirective, lines = headTail(lines)

assert firstDirective.startswith('#basicfuck '), 'invalid first directive'
firstDirective = [part.split('=')[1] for part in firstDirective[11:].split()]

tapeSize, firstDirective = headTail(firstDirective)
tapeSize = int(tapeSize)

cellRange, firstDirective = headTail(firstDirective)
cellRange = tuple(cellRange.split('~'))

overflowBehaviour, firstDirective = headTail(firstDirective)

# Parse second directive
secondDirective, lines = headTail(lines)

assert secondDirective.startswith('#allocate '), 'invalid second directive'
secondDirective = secondDirective[10:]
variables = secondDirective.split(',')

for i, variable in enumerate(variables):
    variable = variable.strip()
    splitByArrow = variable.split('->')

    if len(splitByArrow) > 1:
        variable = Variable(splitByArrow[0], int(splitByArrow[1]))
    else:
        variable = Variable(variable, 1)
    
    variables[i] = variable

# Allocate tape storage
references = []
lastUnusedIndex = 0

def allocate(name, amt):
    global lastUnusedIndex
    references.append((name, lastUnusedIndex))
    lastUnusedIndex += amt

for variable in variables:
    allocate(variable.name, variable.length)

references = dict(references)

# Start compiling!
output = parse(''.join(lines), references)
print(end=output)