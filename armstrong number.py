n=int(input("enter a number"))
last=0
sum=0
num=n
while n>0:
    last=n%10
    sum=sum+(last*last*last)
    n//10
if(num==sum):
    print("entered number is armstrong")
else:
    print("entered number is not armstrong")