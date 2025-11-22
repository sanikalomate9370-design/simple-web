#write python ocde create seprate list for digit fromoriginal list
#which contain didit and alphabet using list compranction

n = int(input("enter a  number of element in list"))
l1=[]
i = 0
while i < n:
    x=int(input("enter a emement in list"))
    l1.insert(i,x)
    i += 1
print(l1)
digit=[ y for y in l1 if(type(y)==int) ]
print(digit)