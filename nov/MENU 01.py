print("WELCOME")
print("***********")
print("MAIN MENU")
print("***********")
print("SELECT YOUR CONVERSION OPTION:-")
print("1) FARENHITE AND CELSIUS")
print("2)CENTIMETER AND INCH")
print("3)METER AND KILOMETER")
print("4)RUPEES AND DOLLAL")
n=float(input("ENTER YOUR OPTION :-"))
if n==1:
    print("1.1)FARENHITE TO CELSIUS")
    print("1.2)CELSIUS TO FARENHITE")
elif n==2:
    print("2.1)CENTIMETER TO INCH")
    print("2.2)INCH TO CENTIMETER")
elif n==3:
    print("3.1)METER TO KILOMETER")
    print("3.2)KILOMETER TO METER")
elif n==4:
    print("4.1)RUPEES TO DOLLAL")
    print("4.2)DOLLAL TO RUPEES")
n=int(input("ENTER YOUR OPTION (input in given format(x.y)):-"))
if n==1.1:
    f=int(input("Enter the degree farenhite:"))
    c=(5/9)*f-32
    print("celsius=",c)
elif n==1.2:
    c=int(input("Enter the degree celsius:"))
    f=(9/5)*c+32
    print("farenhite=",f)
elif n==2.1:
    cm=int(input(""))
    inc=0.394*cm
    print("inchs=",cm)
elif n==2.2:
    inc=int(input(""))
    cm=inc*2.54
    print("inchs=",cm)
elif n==3.1:
    m=int(input(""))
    km=m/1000
    print("kilometer=",km)
elif n==3.2:
    km=int(input(""))
    m=km*0.624371
    print("meter=",m)
elif n==4.1:
    rs=float(input(""))     #1 indian rupee=0.014 dollar(dt.-11/10/19)
    d=rs*0.014
    print("dollar=",d)
elif n==4.2:
    d=float(input(""))    #1 dollar=70.96 indian rupee(dt.-11/10/19)
    rs=d*70.96
    print("rupees=",rs)
