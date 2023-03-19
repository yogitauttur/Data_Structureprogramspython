class Node:
    def __init__(self,item):
        self.left=None
        self.right=None
        self.val=item

class solution:
    def height(self,root,ans=0):
        lf=0
        temp=root
        while True:
            lf+=1
            if temp is None:
                break
            if temp.left is not None:
                temp=temp.left
            else:
                temp=temp.right
        return lf-1
obj=solution()
'''root=Node(1)
root.right=Node(2)
root.left=Node(3)
root.left.left=Node(4)
root.left.left.left=Node(5)
root.left.left.left.left=Node(6)
'''
root=Node(1)
root.right=Node(2)
root.left=Node(3)
root.right.left=Node(4)
root.right.left.right=Node(6)
print("Height of first tree:",obj.height(root))

obj=solution()
root=Node(2)
root.right=Node(1)
root.right.left=Node(3)
print("Height of second tree:",obj.height(root))


        
