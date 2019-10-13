a=int(input("Enter the lenght of ab"))
b=int(input("Enter the length of bc"))
c=int(input("Enter the length of ca"))
if a+b>c or b+c>a or a+c>b:
    print("It can be a triangle")
else :
    print("it can't be a triangle")
