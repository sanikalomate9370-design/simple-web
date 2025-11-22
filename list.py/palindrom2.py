list1=[]
list2=[]
i=0
n = int(input("Enter a number of element in string:"))
while i < n:
    x=int(input("enter a element in list"))
    list1.insert(i,x)
    i += 1
print(list1)
for j in range(len(list1)-1,-1,-1):
    list2.append(list1[j])
print(list2)
if (list1 == list2):
    print("entered list is palindrom")
else:
    print("entered list is not palindrom")