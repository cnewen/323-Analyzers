import wholething as f1


# i[0] prints out the tokens like identifer
# i[1] prints out the lexeme such as the letter

def assignment(hold, identiferCounter):
    operator = False
    for i in hold:
        if i[0] == 'Identifer =' and identiferCounter == 0:
            print("Token:", i[0], "Lexeme: ", i[1])
            print("<Statement List> -> <Statement> | <Statement> <Statement List>")
            print("<Statement> -> <Compound> | <Assign> | <If> | <Return> | <Print> | <Scan> | <While> ")
            print("< Assign > -> < Identifier > = < Expression> \n")
            identiferCounter += 1

        if i[0] == 'OPERATOR =' and i[1] == '=' and identiferCounter == 1:
            print("Token:", i[0], "Lexeme: ", i[1], '\n')
            operator = True

        if identiferCounter >= 1 and operator == True:
            expression(hold, i, identiferCounter)


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


def expression(hold, i, identiferCounter):  # checks expression
    e(i, identiferCounter)

    t(hold, i, identiferCounter)


def e(i, identiferCounter):  # check if + or -
    if i[0] == 'OPERATOR =' and i[1] == '+':
        print("Token:", i[0], "Lexeme: ", i[1])
        print("<Empty> -> Epsilon")
        print("<TermPrime> -> * <Factor> <TermPrime> | / <Factor> <TermPrime> | <Empty>")
        print("<Empty> -> Epsilon")
        print("ExpressionPrime> -> + <Term> <ExpressionPrime> | - <Term> <ExpressionPrime> | <Empty>  \n ")
    if i[0] == 'OPERATOR =' and i[1] == '-':
        print("Token:", i[0], "Lexeme: ", i[1])
        print("<Empty> -> Epsilon")
        print("<TermPrime> -> * <Factor> <TermPrime> | / <Factor> <TermPrime> | <Empty>")
        print("<Empty> -> Epsilon")
        print("ExpressionPrime> -> + <Term> <ExpressionPrime> | - <Term> <ExpressionPrime> | <Empty>  \n ")


def t(hold, i, identiferCounter):  # checks if an identifier

    if i[0] == 'Identifer =' and identiferCounter == 1:
        print("Token:", i[0], "Lexeme: ", i[1])
        print("<Expression> -> <Term> <ExpressionPrime>")
        print(
            "<Term> -> <Factor> <TermPrime> ")
        print("<Factor> -> - <Primary> | <Primary>")
        print("<Primary> -> <Identifier> | <Integer> | <Identifier> ( <IDs> ) | ( <Expression> ) | <Real> | true | false \n")
    
        identiferCounter += 1

    if i[1] == ';' and identiferCounter >= 1:
        print("Token:", i[0], "Lexeme: ", i[1])
        print("<Empty> -> Epsilon")
        print("<TermPrime> -> * <Factor> <TermPrime> | / <Factor> <TermPrime> | <Empty>")
        print("<Empty> -> Epsilon")
        print("ExpressionPrime> -> + <Term> <ExpressionPrime> | - <Term>  <ExpressionPrime | <Empty>")  
        print("<Empty> -> Epsilon")
        print('-----------end of statement-------\n')
        breakit(hold)
  
        # once end of statement go and check to see if its a new beginning of statement
        # statement(hold) causes recursion to infinite go on


def breakit(hold):
    indexes = [i for i, x in enumerate(hold) if x[1] == ';']  # [4,10,16]
    start = 0
    end = 0

    for y in indexes:
        if start == 0 and end == 0:
            end = y
            for k in hold[start:end+2]:
                statement(k)
            compare = indexes[0]
            end = indexes[1]
            indexes.pop(0)

            start = y

        if start < end:
            for k in hold[start+2:end+2]:
                statement(k)
            end = indexes[1]
            start = y
            indexes.pop(0)

        if len(indexes) == 1:
            for k in hold:
                statement(k)


def statement(hold):
    identiferCounter = 0

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

        for i in hold:
            if i[1] == '':
                hold.remove(i)

        statement(hold)

        # accesses printTokenList function to properly print without list formatting running py wholething.py
        f1.lexer.writeTokenList(inputToken)


main()


# todo add different lexems and tokens into respective keys and stuff into dictionary look at 362 project python
