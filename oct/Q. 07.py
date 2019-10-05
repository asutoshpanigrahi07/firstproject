a=int(input("enter a 2-digit number")) 
x=int(a/10)
y=a%10
z=(y-x)*9
p=z+a
b=(x-y)*9
c=a-b
if x<y:
    print(p)
else:
    print(c)
