import math
a=int(input("give the value of ab"))
b=int(input("give the value of bc"))
c=int(input("give the value of ca"))
s=1/2*(a+b+c)
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print(area)
