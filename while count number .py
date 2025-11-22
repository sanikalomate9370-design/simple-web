n=int(input("enter anumber"))
num=n
f=int(input("enter a number which you want to count"))
count=0
while n!=0:
    last=n%10
    if(last==f):
        count=count+1
    n=n//10
print(f" your number is:{num} and your finding digit is:{f} and it will occurs:{count} times in number")