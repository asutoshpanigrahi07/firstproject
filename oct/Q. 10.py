e=int(input("enter the mark scored in english"))
m=int(input("enter the mark scored in math"))
c=int(input("enter the mark scored in chemistry"))
p=int(input("enter the mark scored in physic"))
x=int(input("enter the mark scored in computer science"))
a=e+m+c+p+x
print(a)
p=a/5
print(p)
if p < 100 and p >= 60:
    print("1st division")
elif p >= 50 and p < 60:
    print("2nd division")
elif p >= 35 and p < 50:
    print ("3rd division")
else :
    print ("fail")
