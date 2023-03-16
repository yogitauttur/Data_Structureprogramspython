class stack:
    def __init__(self):
        self.items1=['Google','youtube','Gmail','instacks','gitub','Linkedin']
        self.items2=[]
        self.size=-1

    def isEmpty(self):
        if self.size==-1:
            return True
        else:
            return False
    def Undo(self):
        if isEmpty():
            return 0
        else:
            self.size=-1
            val=self.items1.pop()
            self.items2.append(val)
            

    def Redo(self):
        if isEmpty():
            return 0
        else:
            val1=self.items2.pop()
            self.items1.append(val1)

op=stack()
          
while 1:
    print("1. Enter U or u:")
    print("2. Enter R or r:")
    print("3. Exit")

    ch=input("Enter your choice:")
    if ch=='U'or ch=='u':
        op.Undo()
    elif ch=='R' or ch=='r':
        op.Redo()
    elif ch==0:
        break
    print(*items,self=" ")
        
            
