# used for print(, file=f) for  when running python wholething.py
from __future__ import print_function
import os
import re
"""
Preston Phan
Luan Nguyen
Calvin Nguyen
current issues:
cant detect comments,
need spaces between operators to detect operators
cant detect invalid var declarations
cant detect var =22; needs to be var = 22 ;
able to compile using
py wholething.py
python wholething.py
on windows 10 through terminal
"""

operator = "*+-=/><%"

separator = "'(){}[],.!:;"

keywords = ['int', 'float', 'bool', 'true', 'false', 'if', 'else', 'then', 'endif',
            'while', 'whileend', 'do', 'doend', 'for', 'forend', 'input', 'output', 'end', 'or', 'not']


class lexer():
    def __init__(self, fileInput):
        self.fileInput = fileInput

    def isKeyword(self, entry):
        for iterator in keywords:
            if iterator == entry:
                return True
        return False

    def isSeparator(self, entry):
        for iterator in separator:
            if iterator == entry:
                return True
        return False

    def isOperator(self, entry):
        for iterator in operator:
            if iterator == entry:
                return True
        return False

    def isInteger(self, entry):
        if entry.isdigit():
            return True
        return False

    def isRealNumber(self, entry):
        if entry[0].isdigit():  # checks if string starts with a number then goes through the entry to find a . to indicate decimal
            for i in entry:
                if self.isSeparator(i) == True and i == '.':
                    return True
        return False

    def isIdentifier(self, entry):
        # variables cant begin with numbers or underscores, check

        if entry != entry.isdigit() and entry != self.isOperator(entry) and entry != self.isSeparator(entry):
            return True
        return False

    def writeTokenList(self):
        tokenIndex = 0
        with open("output.txt", "w") as f:
            print("Tokens      Lexemes", file=f)
            while tokenIndex < len(self.tokenMachine()):
                # accesses the token within the list
                token = self.tokenMachine()[tokenIndex][0]
                # accesses the lexeme part
                lexeme = self.tokenMachine()[tokenIndex][1]

                print(token, lexeme, file=f)

                tokenIndex += 1
            return print("Write to output file was succesful")

    def tokenMachine(self):

        index = 0
        tokenList = []
        fileInput = self.fileInput.split()

        while index < len(fileInput):

            """"
             | fileInput = self.fileInput.split() |
            splits textfile into a list of words ex: 'Me , llamo Bob'
            becomes ['Me,', 'llamo', 'Bob']
            ex:
            entry =fileInput[0] == ['Me']
                  fileInput[1] == ['llamo']
            """
            entry = (fileInput[index])
            if self.isRealNumber(entry) == True:
                tokenList.append(['REAL NUMBER =', entry])

            elif entry.isspace() == False:
                newEntry = list(entry)
                for i in newEntry:

                    """ if self.isInteger(i) == True:
                        tokenList.append(['Integer =', i]) """
                    if i == '!':
                        tokenList.append(
                            ['SEPERATOR (This is a comment) =', i])
                    elif self.isSeparator(i) == True and i != '!':
                        tokenList.append(['SEPERATOR =', i])

                        # calls the functions above which iterate through tokenbs and checks if true,
            if self.isKeyword(entry) == True:
                tokenList.append(['KEYWORD = ', entry])

            elif self.isInteger(entry) == True:
                tokenList.append(['Integer =', entry])

            elif self.isOperator(entry) == True:
                tokenList.append(['OPERATOR =', entry])

            elif self.isIdentifier(entry) == True:
                sepExist = False
                digExist = False
                comment = False
                for i in entry:
                    if self.isSeparator(i) == True:
                        sepExist = True
                if sepExist == False:
                    tokenList.append(['Identifer =', entry])
                if sepExist == True:
                    entry = re.sub('\ |\?|\.|\!|\/|\;|\:', '', entry)
                    if self.isInteger(entry) == True:
                        digExist = True
                    if digExist == False:
                        tokenList.append(['Identifer =', entry])

            index += 1  # increment index to go through each entry in text file

        return tokenList


def main():
    with open("input.txt", "r") as file:
        content = file.read()

        # inputs the text file into the lexer class as var of inputToken
        inputToken = lexer(content)

        # returns a list output which is saved
        lexer.tokenMachine(inputToken)
        # accesses printTokenList function to properly print without list formatting running py wholething.py
        lexer.writeTokenList(inputToken)


main()


"""
input.txt
! Declare and assign a number !
int number;
number = 9; 
15.123 
"""


"""
output
Tokens      Lexemes
SEPERATOR (This is a comment) = !
Identifer = 
Identifer = Declare
Identifer = and
Identifer = assign
Identifer = a
Identifer = number
SEPERATOR (This is a comment) = !
Identifer = 
KEYWORD =  int
SEPERATOR = ;
Identifer = number
Identifer = number
OPERATOR = =
Integer = 9
SEPERATOR = ;
Integer = 1
Integer = 5
SEPERATOR = .
Integer = 1
Integer = 2
Integer = 3
"""
