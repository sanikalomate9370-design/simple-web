num = [1,5,98,45,76,35]
n = int(input("enter value which you want to find"))
i = 0
while i < len(num):
    if(num[i] == n):
        print("value found at index:",i)
        break
    else:
        print("finding...")

    i += 1


