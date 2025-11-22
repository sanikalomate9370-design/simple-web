sub1 =int(input("enter a marks of 1st subject"))
sub2 =int(input("enter marks of 2nd subject"))
sub3 =int(input("enter a marks of 3rd subject"))
tot =sub1+sub2+sub3
avg =tot/3
per =(tot*100)/300
if(per>90):
    print("your grade is A")
elif(per<=90 and per>70):
    print("your grade is B")
elif(per<=70 and per>50):
    print("your grade is C")
elif(per<=50 and per>35):
    print("your grade is D")
else:
    print("sorry you are fail")
