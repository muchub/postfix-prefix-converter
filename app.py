# expression
expression = "A+B*C/(E-F)"  # debug expression

# stack array
stack = []

# postfix/prefix 2D array
arrConvert = [
    [],  # postfix
    []  # prefix
]

# Convert expression to backward
def convertExpression(infix):
    string = []
    for i in range(len(list(infix))):
        string.append(infix[i])
    i = len(string) - 1
    while(i >= 0):
        if(string[i] == ")"):
            string.append("(")
            string.pop(i)
        elif(string[i] == "("):
            string.append(")")
            string.pop(i)
        else:
            string.append(string[i])
            string.pop(i)
        i = i - 1
    return string

# check operation priority
def checkOpr(symbol):
    operation = [
        ['+', '-', '*', '/', '^'],
        [1, 1, 2, 2, 3]
    ]
    priority = 0
    for i in range(len(operation[0])):
        if(symbol == operation[0][i]):
            priority = operation[1][i]
    return priority

# convert array to string
def convertStr(array):
    string = ""
    for i in range(len(array)):
        string = string + str(array[i])
    return string

# check stack loc
def checkStack(stackLoc, i):
    if((stackLoc - 1) != -1):
        if(checkOpr(stack[stackLoc]) == checkOpr(stack[stackLoc - 1])):
            arrConvert[i].append(stack[stackLoc - 1])
            stack.pop(stackLoc - 1)
        elif(checkOpr(stack[stackLoc]) < checkOpr(stack[stackLoc - 1])):
            arrConvert[i].append(stack[stackLoc - 1])
            stack.pop(stackLoc - 1)

# convert to postfix/prefix function
def convert(infix, e):
    for i in range(len(list(infix))):
        if(infix[i] == "+" or infix[i] == "-" or infix[i] == "*" or infix[i] == "/" or infix[i] == "^"):
            stack.append(infix[i])
            stackLen = len(stack)
            j = 0
            while(j < stackLen):
                j = j + 1
            checkStack(j - 1, e)
        elif(infix[i] == "(" or infix[i] == ")"):
            stack.append(infix[i])
            if(infix[i] == ")"):
                j = len(stack) - 1
                while(j >= 0):
                    if(str(stack[j]) == ")"):
                        stack.pop(j)
                    elif(str(stack[j]) == "("):
                        stack.pop(j)
                        break
                    else:
                        arrConvert[e].append(stack[j])
                        stack.pop(j)
                    j = j - 1
        else:
            arrConvert[e].append(infix[i])

    i = len(stack) - 1
    while(i >= 0):
        arrConvert[e].append(stack[i])
        stack.pop(i)
        i = i - 1

convert(expression, 0)  # send to function for postfix
convert(convertExpression(expression), 1)  # send to function for prefix

print("Postfix:-")
print(convertStr(arrConvert[0]))
print("")
print("Prefix:-")
print(convertStr(convertExpression(arrConvert[1])))