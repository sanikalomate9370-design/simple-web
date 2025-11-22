
n =int(input("enter a number fo elements in list you want"))
i = 0
palindrom =[]
count = 0
while i < n:
    x =int(input("eneter a element in list"))
    palindrom.insert(i,x)
    i += 1
print("entered list is",palindrom)

if (i <= len(palindrom)):
    z= palindrom[i]
    elif(len(palindrom) <= i):
        y=palindrom[len(palindrom)]
        elif(= == y ):
            count += 1

        len(palindrom) -= 1
    i += 1
if (count <> 0):
    print("list is palindrom")
else:
    print("list is not palindrom ")

