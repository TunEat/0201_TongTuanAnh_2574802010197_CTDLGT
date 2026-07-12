#bai 9
# Bài 9: Infix -> Postfix


def priority(op):

    if op in "+-":
        return 1

    if op in "*/":
        return 2

    return 0



def infix_to_postfix(exp):

    stack=[]
    result=[]


    for c in exp:


        if c.isalnum():

            result.append(c)


        elif c=="(":

            stack.append(c)


        elif c==")":

            while stack[-1]!="(":
                result.append(stack.pop())

            stack.pop()


        else:

            while stack and priority(stack[-1]) >= priority(c):
                result.append(stack.pop())

            stack.append(c)



    while stack:
        result.append(stack.pop())


    return "".join(result)



exp="a+b*c"

print(infix_to_postfix(exp))