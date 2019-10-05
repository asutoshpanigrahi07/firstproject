#persontype
print("Welcome")
print("MAIN MENU")
print("===***===")
print("1.MALE")
print("2.FEMALE")
print("Choice your gender :-")
g=int(input("->"))
if g==2: 
    a=input("Enter your name :")
    e=int(input("Enter your age :"))
    if e<=16:
          print("how are you beta?")
          h=input()
          if h=="fine":
              print("start your study")
          else:
              print("every thing will be all right")
    elif 16<e>=25:
          print("Hi,how are you?")
          h=input()
          if h=="fine":
              print("start your study fool")
          else:
              print("every thing will be all right")
    else:
          print("how are you mam?")
          h=input()
          if h=="fine":
              print("start your work")
          else:
              print("every thing will be all right")
elif g==1:
    a=input("Enter your name :")
    e=int(input("Enter your age :"))
    if e<=16:
          print("how are you beta?")
          h=input()
          if h=="fine":
              print("start your study")
          else:
              print("every thing will be all right")
    elif 16<e<=25:
          print("Hi,how are you?")
          h=input()
          if h=="fine":
              print("start your study bro")
          else:
              print("every thing will be all right")
    else:
          print("how are you sir?")
          h=input()
          if h=="fine":
              print("start your work")
          else:
              print("every thing will be all right")
else:
    print("Other gender persons are not permeted to use it")
    print("{ERROR}  {ERROR}  {ERROR}")
    print("{ERROR}  {ERROR}  {ERROR}")
