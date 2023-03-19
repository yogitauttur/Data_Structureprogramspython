v,e=map(int,input().split())
graph=[]
for i in range(v):
    n=list(map(str,input().split()))
    graph.append(n)

print(graph)
# To form the adjacency matrix
matrix=[]
for i in range(v):
    temp=[]
    for j in range(v):
        if str(j) in graph[i]:
            temp.append(1)
        else:
            temp.append(0)
    matrix.append(temp)

# to print the adjacency matrix
for row in matrix:
    print(*row,sep=' ')

flag=True
for row in matrix:
    if sum(row)//2==0:
        flag=False
        break
if flag==True:
    print(1)
else:
    print(0)
        

