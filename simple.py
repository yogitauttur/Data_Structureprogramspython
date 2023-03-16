def check1(n):
    print(n)
    n=n**n
    print(n)
    return n

def check2(data):
    print(data)
    data[2]=100

n=3
n=check1(n)

d=[1,2,3,4]
check2(d)
print(n,d)

print()
data1=[1,2,3,4,5]

data2=data1
data3=data1.copy()

data1[2]=500
print(data1,data2,data3)
