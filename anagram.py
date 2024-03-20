str1=input("enter the first string")
str2=input("enter the second string")
str1_sorted=sorted(str1)
str2_sorted=sorted(str2)
if(str1_sorted==str2_sorted):
    print(str1,"and",str2,"are angram")
else:
    print(str1,"and",str2,"are not angram:")
