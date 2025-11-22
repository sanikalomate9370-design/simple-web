#write a python program to create a set by accepting n element from user such as 0-9,A-Z,a-Z
#count the number of digit,uppercase,lowercase
n=int(input("enter a number of elements in set"))
set1= set()
for i in range(n):
    y=input("enter a element")
    set1.add(y)

    
    
print("the given set is",set1)
print("the length of set is :",len(set1))
digit=0
uppercase=0
lowercase=0
for x in set1:
    if('9' <= x >= '0'):
        digit += 1
    elif( 'a' <= x >='z'):
        lowercase += 1
    else:
        uppercase += 1
print("digits are:",digit)
print("uppercses are:",uppercase)
print("lowercases are",lowercase)


