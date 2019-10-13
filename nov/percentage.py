m=int(input("Enter the mark occupied in math:"))
p=int(input("Enter the mark occupied in physics:"))
c=int(input("Enter the mark occupied in chemistry:"))
t=m+p+c
p=(t/300)*100
if p>90:
    print("You got 'A' gread in exam")
    print("You passed in exam")
elif 80<p<90:
    print("You got 'B' gread in exam")
    print("You passed in exam")
elif 60<p<80:
    print("You got 'C' gread in exam")
    print("You passed in exam")
elif 45<p<60:
    print("You got 'D' gread in exam")
    print("You passed in exam")
elif 35<p<45:
    print("You got 'E' gread in exam")
    print("You just passed in exam")
else:
    print("You got 'F' gread in exam")
    print("You failed in exam")
