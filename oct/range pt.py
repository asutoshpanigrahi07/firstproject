#print the range from 1 to 40
print("Which bit of question 10 you want to execute")
print("1.It will print the range given in book")
print("2.It will print the range given in book")
c=int(input("enter your choise:"))
if c==1:
    for i in range(1,41,3):
        print(i,end='')
else:
    for i in range(1,41,3):
        print(i,end='')
        if i%2==0:
            
