num = (1,64,86,35,76,87)
i=0
x=int(input("enter a value which you want to find in tuple"))
while i < len(num):
    if (num[i] == x):
        print("the value u want to find is present at position:",i)
    i += 1
    
