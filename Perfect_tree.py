class Node:
    def __init__(self,item):
        self.key=item
        self.left=None
        self.right=None

def calculate_Depth(root):
    d=0
    while root is not None:
        d+=1
        root=root.left
    return d

def is_perfect(root,d,level=0):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return (d==level+1)
    if root.left is None or root.right is None:
        return False
    return (is_perfect(root.left,d,level+1)and is_perfect(root.right,d,level+1))

root=None
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
root.left.left.left=Node(8)
root.left.left.right=Node(9)
root.left.right.left=Node(10)
root.left.right.right=Node(11)

if is_perfect(root,calculate_Depth(root)):
    print("The tree is perfect tree")
else:
    print("The tree is not perfect tree")
        
