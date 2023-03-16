def parcheker(expr):
    stack=[]
    for i in expr:
        if i in '([{':
            stack.append(i)
        else:
            stack.pop()
    return len(stack)

expr='()[](){}{[]}'
val=parcheker(expr)
if val==0:
    print("True")
else:
    print("False")

