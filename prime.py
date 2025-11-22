n=int(input("enter a number to check"))
c=0
i=2
while i < n:
    if(n%i == 0):
        c=1
    i += 1
if(c==0):
    print("number is prime")
else:
    print("number is not prime")

