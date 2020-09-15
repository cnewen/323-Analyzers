import wholething as f1


# i[0] prints out the tokens like identifer
# i[1] prints out the lexeme such as the letter
class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        return
    def has_value(self,value):
        if self.data == value:
            return True
        else:
            return False

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        return
    def add_list_item(self, item):
        if not isinstance(item, ListNode):
            item = ListNode(item)
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item 

        self.tail = item

        return
    def output_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

        return

def assignment(hold, identiferCounter):
    for i in hold:
        if i[0] == 'Identifer =' and identiferCounter == 0:
            # print(i)
            print(i[0], i[1])
            print("<Statement List> -> <Statement> | <Statement> <Statement List>")
            print("< Assign > -> < Identifier > = < Expression> \n")
            identiferCounter += 1

        if i[0] == 'OPERATOR =' and i[1] == '=' and identiferCounter == 1:
            print(i[0], i[1], "\n")
            # identiferCounter -= 1

        elif identiferCounter >= 1:
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
        print(i[1], ' <-----LEXEME \n')
        print('<Term Prime> -> epsilon')
        print('<Expression Prime> -> + <Term> <Expression Prime> \n')
    if i[0] == 'OPERATOR =' and i[1] == '-':
        print('<Term Prime> -> epsilon')
        print('<Expression Prime> -> + <Term> <Expression Prime> \n')


def t(hold, i, identiferCounter):  # checks if an identifier

    if i[0] == 'Identifer =' and identiferCounter == 1:
        print(i[0], i[1])
        print("<Expression> -> <Term> <ExpressionPrime>")
        print(
            "<Term> -> <Factor> <TermPrime> ")
        print("<Factor> -> - <Identifer> \n")

        identiferCounter += 1
    if i[1] == ';' and identiferCounter >= 1:
        print('token', i[0], ',', 'lexem', i[1], '\n')
        print('|')
        print('v')
        print('<Empty> -> Epsilon')
        print('<ExpressionPrime> -> + <Term> <ExpressionPrime> | - <Term> <ExpressionPrime> | <Empty> \n')
        print('-----------end of statement-------')
        # once end of statement go and check to see if its a new beginning of statement
        #statement(hold) causes recursion to infinite go on


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

        lexer = SingleLinkedList()
        for i in hold:
            lexer.add_list_item(i)
        lexer.output_list()

        #statement(hold)

        # accesses printTokenList function to properly print without list formatting running py wholething.py
        #f1.lexer.writeTokenList(inputToken)


main()


# todo add different lexems and tokens into respective keys and stuff into dictionary look at 362 project python
