# expression input
expression = input("Enter Expression: ")  # debug expression

# Stack
stackTop = 0
stackMax = 2
stack = []

# Push on stack
def push(string):
    global stackTop
    global stackMax
    if(stackTop == stackMax):
        print("stackFull")
    else:
        stack.append(string)
        stackTop = stackTop + 1
        return stackTop

# Pop from stack
def pop():
    global stackTop
    if(stackTop == 0):
        print("stackEmpty")
    else:
        stack.pop()
        stackTop = stackTop - 1

# Convert expression to backward
def reverseExpression(infix):
    string = ""
    i = len(infix) - 1
    while(i >= 0):
        if(infix[i] == ")"):
            string = string + "("
        elif(infix[i] == "("):
            string = string + ")"
        else:
            string = string + str(infix[i])
        i = i - 1
    return string

# check operation priority
def checkOpr(symbol):
    priority = 0
    if(symbol == "+" or symbol == "-"):
        priority = 1
    if(symbol == "*" or symbol == "/"):
        priority = 2
    if(symbol == "^"):
        priority = 3
    return priority

# convert to postfix/prefix function
def convert(infix):
    output = ""
    global stackTop
    for i in range(len(list(infix))):
        if(infix[i] == "+" or infix[i] == "-" or infix[i] == "*" or infix[i] == "/" or infix[i] == "^"):
            push(infix[i])
            stackLoc = stackTop - 1 #stack location
            if((stackLoc - 1) != -1):
                if(checkOpr(stack[stackLoc]) <= checkOpr(stack[stackLoc - 1])): #check priority
                    output = output + str(stack[stackLoc - 1])
                    stack.pop(stackLoc - 1)
                    stackTop = stackTop - 1
        elif(infix[i] == "(" or infix[i] == ")"):
            push(infix[i])
            if(infix[i] == ")"):
                j = stackTop - 1
                while(j >= 0):
                    if(stack[j] == ")"):
                        pop()
                    elif(stack[j] == "("):
                        pop()
                        break
                    else:
                        output = output + str(stack[j])
                        pop()
                    j = j - 1
        else:
            output = output + str(infix[i])
    i = stackTop - 1
    while(i >= 0):
        output = output + str(stack[i])
        pop()
        i = i - 1
    return output

print("\nPostfix:-\n" + convert(expression))
prefix = convert(reverseExpression(expression))
print("\nPrefix:-\n" + str(reverseExpression(prefix)))