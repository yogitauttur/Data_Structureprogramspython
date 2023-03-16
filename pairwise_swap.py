class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode

    def pairwise_swap(self):
        temp=self.head
        nxt=self.head
        while nxt.next!=None:
            nxt=temp.next
            temp.data,nxt.data=nxt.data,temp.data
            temp=nxt.next
        
                 
    def show(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end=' ')
            temp=temp.next

n=int(input("Enter the size of list:"))
data=list(map(int,input().split()))
obj=LinkedList()
for ele in data:
    obj.insert(ele)

obj.pairwise_swap()
obj.show()
               
