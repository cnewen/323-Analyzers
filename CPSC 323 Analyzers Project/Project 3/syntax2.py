import wholething as f1

# i[0] prints out the tokens like identifer
# i[1] prints out the lexeme such as the letter


def directionfunction(table, values, hold):
    isAssignment = False
    stack = []
    stack.clear()
    tracker = []
    indexcounter = 0
    termz = []
    instrtable = ['PUSHI', 'PUSHM', 'POPM', 'ADD']
    test = []
    rulestack = []

    termcount = 0
    stack.append(1)

    for i in hold:
        if i[0] == 'Identifer =' and stack[0] == 1:
            # print(i)
            print("Token:", i[0], "Lexeme", i[1])

            stack.insert(0, 10)
            text = i[0]
            for j in table:
                if j[0] == i[1] and j[3] == 1:
                    rulestack.append(j[1])
                if j[0] == i[1] and j[3] == 0:
                    j[3] += 1

            termz.append(i[1])

        if i[0] == 'OPERATOR =' and i[1] == '=' and stack[0] == 10:
            print('TOKEN:', i[0], "Lexeme  ", i[1], "\n")
            stack.insert(0, 20)
            text = i[0]
            termz.append(i[1])

        if i[0] == 'Identifer =' and stack[0] == 20:
            if termcount == 0:
                print("Token:", i[0], "Lexeme", i[1])
                termz.append(i[1])

                termcount += 1
                stack.insert(0, 30)
                for j in table:
                    if j[0] == i[1] and j[3] == 1:
                        rulestack.append(j[1])

            elif termcount == 1:
                print("Token:", i[0], "Lexeme", i[1])
                termz.append(i[1])

                termcount -= 1
                stack.insert(0, 30)
                for j in table:
                    if j[0] == i[1] and j[3] == 1:
                        rulestack.append(j[1])

        if i[0] == 'Integer =' and stack[0] == 20:

            print("Token:", i[0], "Lexeme", i[1])
            table[indexcounter].append(i[1])
            indexcounter += 1

            stack.insert(0, 30)

        if i[0] == 'OPERATOR =' and (i[1] == '+' or i[1] == '-') and stack[0] == 30:
            print("Token:", i[0], "Lexeme", i[1])
            termz.append(i[1])
            table.append(i[1])

            stack.insert(0, 20)

        if i[0] == 'SEPERATOR =' and stack[0] == 30:
            print("Token:", i[0], "Lexeme: ", i[1])

            stack.insert(0, 40)

        if i[1] == '$' and stack[0] == 40:
            stack.insert(0, 1)

    else:
        stack.insert(0, -1)

    for j in table:
        if j[0] == '$':
            table.remove(j)
    with open("output.txt", "w") as a:
        for y in table:
            if y == '+':
                print('PUSHI', rulestack[-1], file=a)
                rulestack.pop(-1)
                print('PUSHI', rulestack[-1], file=a)
                rulestack.pop(-1)
                print('ADD', file=a)
                print('POPM', rulestack[-1], file=a)
            if y != '+':
                print('PUSHI', y[4], file=a)
                print('POPM', y[1], file=a)
        for y in table:
            if y[0] == '+':
                table.remove(y)
        print('\n', file=a)
        print('Symbol Table', file=a)
        print('Identifer  Memory-Location Type', file=a)
        for y in table:

            print(y[0], "     ",   y[1], "     ",    y[2], file=a)


def assignment(hold, stack):
    uniquelist = []
    uniquevalues = []
    table = []
    count = 0
    position = 0
    rulecount = 0

    for x in stack:
        if x[0] not in uniquelist:
            uniquelist.append(x[0])
        if x[1] not in uniquevalues:
            uniquevalues.append(x[1])

    for y in uniquelist:
        table.append([y, uniquevalues[count], 'integer', rulecount])
        count += 1
    tracker = []
    stack.clear()
    directions = []
    memory = 0

    counter = 0
    indexlist = []
    values = []
    combine = ''

    firstnumb = 0
    # grabs the indexes of =
    for index, (a, b) in enumerate(zip(hold, hold[1:])):

        if a[1] == '=':
            indexlist.append(index)
        if a[0] == 'Integer =' and b[0] == 'Integer =':
            # a[1] = (a[1]+b[1])
            continue

        # 7,12 ,17, 21  where = occurs
    for i, b in zip(indexlist, indexlist[1:]):
        for z in hold[i:b]:
            if z[0] == 'Integer =':
                counter += 1

                values.append(z[1])
            if z[1] == '=' and counter != 0:
                counter = 0

    directionfunction(table, values, hold)


def declarative(hold, stack):
    declarativeTrue = False
    dirstack = []
    Memory_address = 2000

    for i, j in zip(hold, hold[1:]):
        if i[0] == 'KEYWORD = ' and len(dirstack) == 0:
            dirstack.insert(0, 'PUSHI')

        if i[0] == 'Identifer =' and dirstack[0] == 'PUSHI':

            dirstack.insert(0, 'POPM')
            stack.append([i[1], Memory_address])
            Memory_address += 1

        if i[0] == 'Identifer =' and dirstack[0] == 'POPM':
            dirstack.insert(0, 'PUSHI')
            stack.append([i[1], Memory_address])
        if i[0] == 'SEPERATOR =' and j[1] == ';':
            stack.append([i[1], Memory_address])


def statement(hold, stack):
    # stack.append(1)
    declarative(hold, stack)
    assignment(hold, stack)


def main():
    with open("input.txt", "r") as file:
        content = file.read()

        # inputs the text file into the lexer class as var of inputToken
        inputToken = f1.lexer(content)

        # returns a list output which is saved
        f1.lexer.tokenMachine(inputToken)

        hold = f1.lexer.tokenMachine(inputToken)

        stack = []
        for i in hold:
            if i[1] == '':
                i[1] = '$'

        statement(hold, stack)


main()


# todo add different lexems and tokens into respective keys and stuff into dictionary look at 362 project python
