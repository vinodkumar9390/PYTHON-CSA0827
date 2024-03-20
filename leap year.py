year=int(input("enter the given year:"))
if(year<0):
    print("we can't year negtive number years")
elif(year%4==0 and year%100!=0):
    print(year,"is a leap year")
elif(year%100==0 and year%400==0):
    print(year,"is a leap year")
else:
    print(year,"is non leap year")