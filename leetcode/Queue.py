class Queue:
    data=[]
    def __init__(self):
        data=[]
    def push(self,x):
        self.data.append(x)
    def pop(self):
        v=self.data.pop(0)
        print(v,' is being popped out')
    def search(self,x):
        if x in self.data:
            print(x,'is present the Queue')
        else:
            print(x,'is not present the Queue')
    def display(self):
        print(self.data)


c=0
myqueue = Queue()
while c<5:
    print("MAIN MENU")
    print("1.Add a element to the stack")
    print("2.Remove a element from the stack")
    print("3.Search")
    print("4.Display all")
    print("5.Exit")
    c=int(input("Enter your option:"))
    
    print("")
    
    if c==1:
        a=int(input("Enter the number you want to add:"))
        myqueue.push(a)
    elif c==2:
        myqueue.pop()
    elif c==3:
        a=int(input("Enter the number you want to search:"))
        myqueue.search(a)
    elif c==4:
        myqueue.display()