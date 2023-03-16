class Node:
    def __init__(self,item):
        self.left=None
        self.right=None
        self.val=item

def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val)+"->",end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(str(root.val)+"->",end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val)+"->",end=" ")

def search(root,number):
   
    if root==None:
        return 0
    elif number==root.val:
        return root.val
    elif number<root.val:
        return search(root.left,number)
    elif number>root.val:
        return search(root.right,number)
    else:
        return 0

def insert(root,num):
   
    if root==None:
        return Node(num)
    elif root.val<num:
        root.right=insert(root.right,num)
    elif root.val>num:
        root.left=insert(root.left,num)
    return root

def minvalueNode(root):
    current=root
    while current.left is not None:
        current=current.left
    return current

def deleteNode(root,key):
    if root is None:
        return root
    if key<root.val:
        root.left=deleteNode(root.left,key)
    elif key>root.val:
        root.right=deleteNode(root.right,key)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        temp=minvalueNode(root.right)
        root.val=temp.key
        root.right=deleteNode(root.right,temp.key)
    return root

'''
root=Node(8)
root.left=Node(3)
root.right=Node(10)
root.righ.right=Node(14)
root.left.left=Node(1)
root.left.right=Node(6)
root.left.right.left=Node(4)
root.left.right.right=Node(7)
        


root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
root.left.left.left=Node(8)
root.left.left.right=Node(9)
root.right.right.right=Node(10)
root.right.right.left=Node(11)



print("\n Preorder traversal:")
preorder(root)
print("\n PostOrder traversal:")
postorder(root)
'''

root=None
root=insert(root,8)
root=insert(root,3)
root=insert(root,1)
root=insert(root,6)
root=insert(root,7)
root=insert(root,10)
root=insert(root,14)
root=insert(root,4)
n=int(input("\n Enter the Search element:"))
s=search(root,n)
if s==n:
    print("Search element is found:",s)
else:
    print(n,"this Search element is not found")

print("\n Inorder Traversal:")
inorder(root)
print("\n Preorder traversal:")
preorder(root)
print("\n PostOrder traversal:")
postorder(root)

print("\n Delete 10")
root=deleteNode(root,10)
print("After deleting the element Inorder Traversal:")
inorder(root)
