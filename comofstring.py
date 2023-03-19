from itertools import permutations
s=set()
str1=input("Enter the string:")
combinations=permutations(str1)
print(combinations)
#
for ele in combinations:
    str2=' '.join(ele)
    print(str2)
    if str2==str2[ : :-1]:
        s.add(str2)
print(s)
