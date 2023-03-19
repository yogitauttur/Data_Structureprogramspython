class solution:
    def maxPathSum(self,root):
        mx=float('-inf')
        def maxsum(r):
            nonlocal mx
            if not r:
                return float('-inf')
            if not r.left and not r.right:
                return r.data
            l=maxsum(r.left)
            ri=maxsum(r.right)
            mx=max(mx,l+ri+r.data)
            return r.data+max(l,ri)
        y=maxsum(root)
        if not root.left or not root.right:
            return max(y,mx)
        return mx

from collections import deque
import sys
sys.setrecursionlimit(10**6)
class Node:
    def __init__(self,val):
        self.right=None
        self.data=val
        self.left=None

def buildTree(s):
    if(len(s)==0 or s[0]=="N"):
        return None
    ip=list(map(str,s.split()))
    root=Node(int(ip[0]))
    size=0
    q=deque()
    q.append(root)
    size=size+1
    i=1
    while(size>0 and i<len(ip)):
        currNode=q[0]
        q.popleft()
        size=size-1
        currval=ip[i]
        if currval!="N":
            currNode.left=Node(int(currval))
            q.append(currNode.left)
            size=size+1
        i=i+1
        if i>=len(ip):
            break
        currval=ip[i]
        if currval!="N":
            currNode.right=Node(int(currval))
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob=solution()
        print(ob.maxPathSum(root))
            
    
    
