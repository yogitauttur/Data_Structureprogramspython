l1=[-1,-1,-2,3,4]
c1=0
count=0
for i in l1:
    if i<0 and not i==0:
        c1+=1
    if i<0 and not i==0:
        count+=1
    if not i==0 and i>0:
        result=0

print(c1)
print(count)

mul=1
mul1=1
if c1//2==0:
    for i in l1:
        mul=mul*i
if count//2!=0:
    for i in l1:
        print(i,end=" ")
        mul1=mul1*i
print(mul)
print(mul1)
