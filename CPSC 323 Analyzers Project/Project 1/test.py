import wholething as f1


# i[0] prints out the tokens like identifer
# i[1] prints out the lexeme such as the letter

def assignment(hold, identiferCounter):
    for i in hold:
        if i[0] == 'Identifer =' and identiferCounter == 0:
            # print(i)
            print(i[0], i[1])
            print("<Statement List> -> <Statement> | <Statement> <Statement List>")
            print("< Assign > -> < Identifier > = < Expression> \n")
            identiferCounter += 1

        if i[0] == 'OPERATOR =' and i[1] == '=' and identiferCounter == 1:
            print(i[0], i[1], "START OF EXPRESSION")
            #identiferCounter -= 1

        if identiferCounter >= 1:
            expression(i, identiferCounter)


def declarative(hold):
    declarativeTrue = False
    for i in hold:
        if i[0] == "KEYWORD =":
            declarativeTrue = True
            print(i[0], i[1])
            print("<Statement List> -> <Statement> | <Statement> <Statement List>")
            print(
                "<Statement> -> <Compound> | <Assign> | <If> | <Return> | <Print> | <Scan> | <While> ")
            print("< Declarative > -> < Type > < Identifer > \n")
            return declarativeTrue


def expression(i, identiferCounter):  # checks expression
    e(i, identiferCounter)

    t(i, identiferCounter)


def e(i, identiferCounter):  # check if + or -
    if i[0] == 'OPERATOR =' and i[1] == '+':
        print(i)
        print('<Term Prime> -> epsilon')
        print('<Expression Prime> -> + <Term> <Expression Prime>')
    if i[0] == 'OPERATOR =' and i[1] == '-':
        print('<Term Prime> -> epsilon')
        print('<Expression Prime> -> + <Term> <Expression Prime>')


def t(i, identiferCounter):  # checks if an identifier

    if i[0] == 'Identifer =' and identiferCounter == 1:
        print(i[0], i[1])
        print("<Expression> -> <Term> <ExpressionPrime>")
        print(
            "<Term> -> <Factor> <TermPrime> ")
        print("<Factor> -> - <Identifer> \n")

        identiferCounter += 1


def statement(hold):
    identiferCounter = 0
    index = 1
    statementTrue = True
    equalsign = False
    plusminus = False
    multdivide = False

    assignment(hold, identiferCounter)
    # check if assignment has an expression
    # check the expression if its arithmetic

    declarative(hold)


def main():
    with open("input.txt", "r") as file:
        content = file.read()

        # inputs the text file into the lexer class as var of inputToken
        inputToken = f1.lexer(content)

        # returns a list output which is saved
        f1.lexer.tokenMachine(inputToken)

        hold = f1.lexer.tokenMachine(inputToken)

        statement(hold)

        # accesses printTokenList function to properly print without list formatting running py wholething.py
        f1.lexer.writeTokenList(inputToken)


main()


# todo add different lexems and tokens into respective keys and stuff into dictionary look at 362 project python
