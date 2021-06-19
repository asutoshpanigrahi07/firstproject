class sll:
    def __init__(self,value):
        self.value=value
        self.nextnode=None
        
    def add(self,value):
        node=sll(value)
        if self==None:
            self=node
        else:
            node.nextnode=self
            self=node
        return self

    def display(self):
        temp=self
        print("Nodes=>")
        while temp!=None:
            print(temp.value, end = " ")
            temp=temp.nextnode
        print("")

    def addend(self,value):
        temp = self
        if(temp == None):
            return self.add(value, None)
        node = sll(value)
        while(temp.nextnode != None):
            temp = temp.nextnode
        temp.nextnode = node;
        return self;
    
    def search(self,x):
        temp=self
        while (temp != None):
            if temp.value==x:
                print(temp.value,'is present in the linked list')
                return
            temp=temp.nextnode
        print("Not present")

    def remove(self):
        temp=self
        if temp==None:
            print("no data is present")
        else:
            self=self.nextnode
            return self

    def removeend(self):
        temp=self
        if temp==None:
            print("no data is present")
            return self
        if temp.nextnode  == None:
            self = None
            return self
        while temp.nextnode.nextnode !=None:
            temp=temp.nextnode
            print(temp.value)
        temp.nextnode=None
        return self

    def removes(self,x):
        temp = self
        if(temp == None):
            return;
        if(temp.nextnode == None and temp.value == x):
            self = None
            return self
        while (temp.nextnode != None):
            if temp.nextnode.value==x:
                temp.nextnode=temp.nextnode.nextnode
                return self
            temp=temp.nextnode
        print(x,"Not found")

    def searchlast(self,x):
        t1=self
        t2=self
        c=x-1
        if(t1 == None):
            return
        if(t1.nextnode == None and t1.value == x):
            self = None
            return self
        while c!=0:
            t2=t2.nextnode
            c=c-1
        while (t2.nextnode!=None):
            t2=t2.nextnode
            t1=t1.nextnode
        print(t1.value,"is the ",x,"termfrom the end")
        return

    def midterm(self,x):
        temp=self
        if(temp == None):
            return;
        if(temp.nextnode == None and temp.value == x):
            self = None
            return self
        count=0
        while temp!=None:
            count+=1
            temp=temp.nextnode
        return count

c=0
q=int(input("Enter the first number of the linked list:"))
head=sll(q)
print("")

while c<9:
    print("MAIN MENU")
    print("1.Add in the beggining")
    print("2.Add in the end")
    print("3.Remove from the beggining")
    print("4.Remove from the end")
    print("5.Remove by searching")
    print("6.Search")
    print("7.Display all")
    print("8.Search the Nth term from the last")
    print("9.Show Mid-term")
    c=int(input("Enter your option:"))

    if c==1:
        a=int(input("Enter the number:"))
        head=head.add(a)
        print("")
    elif c==2:
        a=int(input("Enter the number:"))
        head=head.addend(a)
        print("")
    elif c==3:
        head=head.remove()
        print("")
    elif c==4:
        head=head.removeend()
        print("")
    elif c==5:
        a=int(input("Enter the number:"))
        head=head.removes(a)
        print("")
    elif c==6:
        a=int(input("Enter the number:"))
        head.search(a)
        print("")
    elif c==7:
        head.display()
        print("")
    elif c==8:
        a=int(input("Enter the term:"))
        head.searchlast(a)
        print("")

        
