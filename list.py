gitclass node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None

class singlyll:
    def __init__(self) -> None:
        self.head=None

    def addfront(self,data):
        new_node=node(data)
        if self.head is None:
            self.head= new_node
        else:
            new_node.next=self.head
            self.head=new_node

    def printll(self):
        if self.head is None:
            print('sll is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.next
        
    def addlast(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=new_node

    def addmid(self,data,place):
        n=self.head
        '''i=0
        while i<place:
            n=n.next
            i+=1
        new_node.next=n.next
        n.next=new_node'''
        while n is not None:
            if n.data==place:
                break
            n=n.next
        if n is None:
            print('its not present')
        else:
            new_node=node(data)
            new_node.next=n.next
            n.next=new_node

    def delfront(self):
        if self.head is None:
            print('sll its empty')
        else:
            self.head.next=self.head

    def dellast(self):
        if self.head is None:
            print('list is empty')
        elif self.head.next is None:
            self.head=None
        else:
            n=self.head
            while n.next.next is not None:
                n=n.next
            n.next=None
        
    def delmid(self,x):
        if self.head is None:
            print('ll is empty')
            return
        if self.head.data==x:
            self.head=self.head.next
            return
        n=self.head
        while n.data is not None:
            if n.next.data==x:
                break
            n=n.next
        if n is None:
            print('node is not available')
        else:
            n.next=n.next.next

x=singlyll()
x.addfront(21)
x.addfront(31)
x.addlast(41)
x.addlast(51)
x.addmid(61,21)
#x.delfront()
#x.dellast()
x.delmid(51)
x.printll()