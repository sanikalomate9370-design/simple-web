n =int(input("enter a number of subject"))
sum=0
for i in range(1,n+1):
    marks=int(input(f"enter a marks{i}="))
    sum=sum+marks
print("sum of all subject",sum)
avg=sum/n
print("your avg is",avg)
per=(sum*100)/300
print(f"your percentage is :{per}")
if(per>=90):
    print("your grade is :A")
elif(per>=70 and per<=89):
    print("your grade is B")
elif(per>=50 and per<=79):
    print("your grade is C")
elif(per>=35 and per<=49):
    print("tour grade is d")
else:
    print("sorry u are fail")