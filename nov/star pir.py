n = int(input("enter number"))
for row in range(1,n+1):
    for s in range(1, n-row+1):
        print(" ", end=" ")
    for c in range(1,2*row):
        print(" *",end="")
    print()
for row in range(n-1,0,-1):
    for s in range(n-row+1, 1,-1):
        print(" ", end=" ")
    for c in range(2*row,1,-1):
        print(" *",end="")
    print()
