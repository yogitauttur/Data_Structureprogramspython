def Modify_array(n,k):
    sum1=0
    print(n)
    for i in range(0,k):
       n1=n[0]
       g=-n1
       n.remove(n1)
       n.append(g)
       n=sorting(n)
       print(n)
    print("Sum:",sum(n))
    
def sorting(l1):
    for i in range(0,len(l1)):
        for j in range(0,len(l1)-1):
            if l1[j]>l1[j+1]:
                temp=l1[j]
                l1[j]=l1[j+1]
                l1[j+1]=temp
    return l1


l1=list(map(int,input().split()))
k=int(input())
l2=[]
l2=sorting(l1)
Modify_array(l2,k)
