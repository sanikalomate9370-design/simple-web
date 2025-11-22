n =int(input("enter a number of value you need to insert in list"))
list =[]
i =0
while i < n:
    x =int(input("enter a value in list"))
    list.insert(i,x) #here we need to pass two parameters index and value
    i += 1
print(list)
while i < n:
    x =int(input("enter a value in list"))
    list.append(x)#here we need to pass one paramerte only value
    i += 1
print(list)
