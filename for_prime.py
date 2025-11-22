n = int(input("enter a number"))
i=2
c=0
while i < n:
    if(n%i ==0):
        c = 1
    i += 2
if (c == 0):
    print("entered number is prime")
else:
    print("entered number is not prime"
    )