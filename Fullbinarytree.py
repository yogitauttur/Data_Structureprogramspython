class Node:
    def __init__(self,item):
        self.left=None
        self.right=None
        self.item=item

def isFullTree(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left is not None and root.right is not None:
        return(isFullTree(root.left)and isFullTree(root.right))
    return False

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.left.right.left=Node(6)
root.left.right.right=Node(7)
root.left.right.right.left=Node(8)

if isFullTree(root):
    print("The tree is Full binary tree")
else:
    print("The tree is not Full binary tree")
    
