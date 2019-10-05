a=int(input("enter a 3-digit number"))
b=a%10
c=int(a/10)%10
d=int(a/100)
t=(b*100)+(c*10)+(d)
print(t)
