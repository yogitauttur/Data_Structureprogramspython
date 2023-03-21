def topology(n,m,in3,in4):
    if len(in3)&len(in4)==n:
        return 3
    elif len(in3)&len(in4)<n:
        return 1
    else:
        return 2

n=int(input("Enter the number of nodes:"))
m=int(input("Enter the no of connections:"))
in3=list(map(int,input("Enter the starting point of conn:").split()))
in4=list(map(int,input("Enter ending of conn:").split()))
t=topology(n,m,in3,in4)
if t==1:
    print("Bus topology")
elif t==2:
    print("Star topology")
else:
    print("ring topology")
