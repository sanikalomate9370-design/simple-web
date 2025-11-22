n = int(input("enter a number of element in list"))
i = 1
list = []
while i <= n:
    x = (input(f"enter a element in list {i}"))
    list.insert(i,x)
    i += 1
copy_list=list.copy()
copy_list.reverse()
if(list == copy_list):
    print("number is palindrom")
else:
    print("number is not palindrom")
