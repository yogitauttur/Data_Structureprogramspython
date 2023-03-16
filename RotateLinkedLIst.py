# Rotate LeftShift on Linked List 

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

    '''
        def rotate(self,k,n):
        count=0
        temp=self.head
        while temp!=None:
            count+=1
            if count>k:
                print(temp.data,end=' ')
            temp=temp.next
        count=0
        temp=self.head
        while temp!=None:
            count+=1
            if count<=k:
                print(temp.data,end=' ')
            temp=temp.next
        
       for i in range(k):
           temp=self.head
           temp1=self.head
           while temp.next!=None:
               temp=temp.next
           nxt=temp1.next
           temp1.next=None
           self.head=nxt
           temp.next=temp1
'''
    def palindrome(self):
        temp=self.head
        list1=[]
        while temp!=None:
            list1.append(temp.data)
            temp=temp.next
        if list1==list1[ : :-1]:
            print("True")
        else:
            print("False")

    def even_odd(self):
        temp=self.head
        even=[]
        odd=[]
        while temp!=None:
            if temp.data//2==0:
                even.append(temp.data)
            else:
                odd.append(temp.data)
        print("Even number:",even)
        print("Odd Number:",odd)

for _ in range(int(input("Enter the Number of test cases you want to perform:"))):
               n=int(input("Enter the size of list:"))
               data=list(map(int,input().split()))
               obj=LinkedList()
               for ele in data:
                   obj.insert(ele)
               #k=int(input("Enter the value of k:"))
              # obj.rotate(k,n)
               obj.palindrome()
               obj.even_odd()
            
        
        
