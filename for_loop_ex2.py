tuple = (3,5,7,3,9,5)
n =int(input("enter value you want to find"))
i = 0
for x in tuple:
    if (x == n):
        print("value found at index :",i)
    i += 1
    