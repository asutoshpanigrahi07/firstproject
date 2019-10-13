#n = int(input("enter number"))
for r in range(1,3):
    for s in range(1,3-r+1):
        print(" ", end=" ")
    for c in range(0,r+1):
        print((11**c),end="")
    print()
