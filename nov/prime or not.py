n=int(input("Enter a no. to cheack:"))
c=1
for i in range(1,n):
    if n%i==0:
        c+=1
if c==2:
    print("It is a prime no.")
else:
    print("It is not a prime no.")
