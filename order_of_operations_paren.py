# adds parens for order of operations in logic 
'''
() paren
ㄱ not 
↔and 
Ⅴor 
→ implies
↔ biconditional 
'''

# list of operators in order of their priority in logic
operators = ['ㄱ', 'Λ', 'Ⅴ', '→', '↔']

# statement = input("input: ")
statement = "ㄱ(ㄱ(ㄱㄱb→(aΛbΛcⅤa→dΛeΛf))Ⅴa↔ㄱpΛq→qⅤㄱsⅤ(sⅤr)Λㄱ(sΛv→p))"
print(statement) # checking

# need to build up rather than going through linearly wheee
















def addParenForParen(operators, statement):
    '''
    separates string given a list of operators, statement, assuming all
    variables are 1 letter long
    operators = ['ㄱ', 'Λ', 'Ⅴ', '→', '↔']
    '''
    paren = []
    for i in statement:
    # controlling parenthesies list 
        if char == "(": 
            paren.append("(")  
        elif char == ")":
            paren.pop()

def addParenForOpearator(operator):
    ''' adds parenthesies for a given operator 
    '''
