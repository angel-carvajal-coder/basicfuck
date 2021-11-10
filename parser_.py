from util import *

def parse(code, references):
    statements = code.split(';')
    output = ''

    for statement in statements:
        cellPointer = 0
        statement = statement.strip()
        
        op = '+'
        splitByPlusOrMinusEquals = stripAll(statement.split('+='))
        if len(splitByPlusOrMinusEquals) <= 1:
            op = '-'
            splitByPlusOrMinusEquals = stripAll(statement.split('-='))

        splitByArrow = stripAll(splitByPlusOrMinusEquals[0].split('->'))
        if splitByArrow[0] in references.keys():
            reference = references[splitByArrow[0]]
            reference = reference + (int(splitByArrow[1]) if len(splitByArrow) > 1 else 0)
            cellPointer += reference
            output += '>' * reference

        if len(splitByPlusOrMinusEquals) > 1:
            try:
                output += '+' * int(splitByPlusOrMinusEquals[1])
            except ValueError:
                reference2 = references[splitByPlusOrMinusEquals[1]]
                diff = reference2 - reference
                cellPointer += diff
                output += '>' * diff + '[-' + '<' * diff + op + '>' * diff + ']'

                #output += 
        
        output += '<' * cellPointer
        output += '\n'


    return output