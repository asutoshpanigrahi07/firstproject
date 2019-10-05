m=int(input("enter the initial value"))
n=int(input("enter the final value"))
s=0
if m%2==1:
    for a in range (m,n+1,2):
        print(a)
        s=s+a
    print(s)
else:
    m=m+1
    for a in range (m,n+1,2):
        print(a)
        s=s+a
    print(s)
