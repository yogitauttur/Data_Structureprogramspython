row=int(input())
for i in range(1,row+1):
    for j in range(1,row+1):
        if i+j==row+1 or i==1 or j==5 or i==5 or j==1 or i+j>row:
            print("*",end=" ")
        else:
            print(' ',end=' ')
    print()
