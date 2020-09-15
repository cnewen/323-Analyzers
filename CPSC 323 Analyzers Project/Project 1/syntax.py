import wholething as f1


# i[0] prints out the tokens like identifer
# i[1] prints out the lexeme such as the letter


def test(hold):
    equalsign = False
    plusminus = False
    multdivide = False

    index = 1
    identiferCounter = 0
    for i in hold:
        ## First time assignment
        if i[0] == 'Identifer =' and identiferCounter == 0:
            # print(i)
            print("Token:", i[0], "Lexeme", i[1])
            print("<Statement List> -> <Statement> | <Statement> <Statement List>")
            print(
                "<Statement> -> <Compound> | <Assign> | <If> | <Return> | <Print> | <Scan> | <While> ")
            print("< Assign > -> < Identifier >= < Expression > \n")
            identiferCounter += 1

        ##Following Assignments
        if i[0] == 'Identifer =' and identiferCounter == 1 and equalsign == False and plusminus == False:
            # print(i)
            print("Token:", i[0], "Lexeme", i[1])

            print(
                "<Statement> -> <Compound> | <Assign> | <If> | <Return> | <Print> | <Scan> | <While> ")
            print("< Assign > -> < Identifier >= < Expression > \n ")

            
        ##Equal signs
        if i[0] == 'OPERATOR =' and i[1] == '=':
            equalsign = True
            # print(i)
            print('TOKEN:', i[0], "Lexeme  ", i[1], "\n")

        ##First Term    
        termcount = 0
        if i[0] == 'Identifer =' and termcount == 0 and equalsign == True and plusminus == False:
            print("Token:", i[0], "Lexeme", i[1])
            print("<Expression> -> <Term> <ExpressionPrime>")
            print(
                "<Term> -> <Factor> <TermPrime> ")
            print("<Factor> -> - <Primary> | <Primary>")
            print("<Primary> -> <Identifier> | <Integer> | <Identifier> ( <IDs> ) | ( <Expression> ) | <Real> | true | false \n")
            termcount += 1

        ## + and-
        if i[0] == 'OPERATOR =' and (i[1] == '+' or i[1] == '-') :
            print("Token:", i[0], "Lexeme", i[1])

            plusminus = True
            print("<Empty> -> Epsilon")
            print(
                "<TermPrime> -> * <Factor> <TermPrime> | / <Factor> <TermPrime> | <Empty>")
            print("<Empty> -> Epsilon")
            print("ExpressionPrime> -> + <Term> <ExpressionPrime> | - <Term> ")
            print("<ExpressionPrime> | <Empty>  \n ")

        ##Second Term
        if i[0] == 'Identifer =' and plusminus == True:
            print("Token:", i[0], "Lexeme", i[1])

            print("<Term> -> <Factor> <TermPrime> ")
            print("<Factor> -> - <Primary> | <Primary>")
            print("<Primary> -> <Identifier> | <Integer> | <Identifier> ( <IDs> ) | ( <Expression> ) | <Real> | true | false \n")

        ## * and /
        if i[0] == 'OPERATOR =' and (i[1] == '*' or i[1] == '/') :
            print("Token:", i[0], "Lexeme", i[1])

            multdivide = True
            print("<Empty> -> Epsilon")
            print("<TermPrime> -> * <Factor> <TermPrime> | / <Factor> <TermPrime> | <Empty>  \n ")

        ##Second Term
        if i[0] == 'Identifer =' and multdivide == True:
            print("Token:", i[0], "Lexeme", i[1])

            print("<Term> -> <Factor> <TermPrime> ")
            print("<Factor> -> - <Primary> | <Primary>")
            print("<Primary> -> <Identifier> | <Integer> | <Identifier> ( <IDs> ) | ( <Expression> ) | <Real> | true | false \n")
        ## ;
        if i[0] == 'SEPERATOR =' and i[1] == ';':
            termcount -= 1

            plusminus = False
            equalsign = False
            multdivide = False 
            print("Token:", i[0], "Lexeme", i[1])
            print("<Empty> -> Epsilon")
            print(
                "<TermPrime> -> * <Factor> <TermPrime> | / <Factor> <TermPrime> | <Empty>")
            print("<Empty> -> Epsilon")
            print("<ExpressionPrime> | <Empty> ")

            print("ExpressionPrime> -> + <Term> <ExpressionPrime> | - <Term> \n")


def main():
    with open("input.txt", "r") as file:
        content = file.read()

        # inputs the text file into the lexer class as var of inputToken
        inputToken = f1.lexer(content)

        # returns a list output which is saved
        f1.lexer.tokenMachine(inputToken)

        hold = f1.lexer.tokenMachine(inputToken)

        test(hold)

        # accesses printTokenList function to properly print without list formatting running py wholething.py
        f1.lexer.writeTokenList(inputToken)


main()


# todo add different lexems and tokens into respective keys and stuff into dictionary look at 362 project python
