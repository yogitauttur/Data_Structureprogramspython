class Node:
    def __init__(self,item):
        self.left=None
        self.right=None
        self.val=item
        


def count_leaves(root,count=0):
    
    if root==None:
        return 0
            
    if root.left is None and root.right is None:
        return count+1
    if root.left is not None or root.right is not None:
        return(count_leaves(root.left,count) + count_leaves(root.right,count))
    
def height(root,count=0):
    if root==None:
        return 0
    elif root.left is None and root.right is None:
        return count
    elif root.left is not None or root.right is not None:
        return(height(root.left,count+1)+ height(root.right,count+1))
    

root=Node(4)
root.left=Node(8)
root.right=Node(10)
root.left.left=Node(7)
root.left.right=Node(3)
root.right.left=Node(5)
root.right.right=Node(1)

root.left.left.left=Node(45)
root.left.right.left=Node(18)
root.left.right.right=Node(13)
s=count_leaves(root)
h=height(root)
print("Leaves nodes are:",s)
print("Height of the tree is",h-1)

