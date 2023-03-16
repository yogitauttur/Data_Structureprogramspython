
''' POSTFIX EXPRESSION '''
class evaluate_prefix:
    def __init__(self):
        self.items=[]
        self.size=-1

    def isEmpty(self):
        if self.size==-1:
            return True
        else:
            return False

    def push(self,item):
        self.items.append(item)
        self.size+=1

    def pop(self):
        if self.isEmpty():
            return 0
        else:
            self.size-=1
            return self.items.pop()

    def seek(self):
        if self.isEmpty():
            return False
        else:
            return self.items[self.size]

    def evaluate(self,expr):
        for i in expr:
            if i in "0123456789":
                self.push(i)
            else:
                op1=self.pop()
                op2=self.pop()
                result=self.cal(op1,op2,i)
                self.push(result)
        return self.pop()

    def cal(self,op1,op2,i):
        
        if i=="*":
            return int(op1)*int(op2)
        elif i=="/":
            return int(op1)/int(op2)        
        elif i=="+":
            return int(op1)+int(op2)
        elif i=="-":
            return int(op1)-int(op2)
        elif i=="^":
            return int(op1)^int(op2)

s=evaluate_prefix()
expr=input("Enter expression:")
value=s.evaluate(expr)
print(value)
