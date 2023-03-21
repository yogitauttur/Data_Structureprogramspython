def minProductSubset(a,n):
    if n==1:
        return a[0]
    max_neg=float('-inf')
    min_pos=float('-inf')
    cnt_neg=0
    cnt_zero=0
    prod=1

    for i in range(0,n):
        if a[0]==0:
            cnt_zero=cnt_zero+1
            continue
        if a[i]<0:
            cnt_neg=cnt_neg+1
            max_neg=max(max_neg,a[i])

        if a[i]>0:
            min_pos=min(min_pos,a[i])
        prod=prod*a[i]

    if cnt_zero==n or (cnt_neg==0 and cnt_zero>0):
        return 0
    if cnt_neg==0:
        return min_pos
    if (cnt_neg & 1)==0 and cnt_neg!=0:
        prod=prod//max_neg
    return prod

l1=list(map(int,input().split()))
n=len(l1)
print(minProductSubset(l1,n))
        
