n=int(input("Enter the no. of fibonacii no.:"))
x=0
y=1
if n==1:
    print(x)
elif n==2:
    print(x)
    print(y)
else:    
    print(x)
    print(y)
    for i in range(2,n):
        z=x+y
        print(z)
        x,y=y,x+y
