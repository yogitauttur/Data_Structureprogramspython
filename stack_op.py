stack=list(input().split())
temp=[]
while True:
    ch=input()
    if ch=='U' or ch=='u':
        temp.append(stack.pop())
    elif ch=='R' or ch=='r':
        stack.append(temp.pop())
    elif ch==0:
        break
    print(*stack,sep=' ')
