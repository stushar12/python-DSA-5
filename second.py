class Node(object):
    def __init__(self,data):
        self.data=data
        self.nextNode=None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size=0

    def insertEnd(self,data):

        self.size=self.size+1
        newNode=Node(data)
        
        actualNode=self.head
        
        if not self.head:
            self.head=newNode
        else:
            while actualNode.nextNode is not None:
                actualNode=actualNode.nextNode
            actualNode.nextNode=newNode
    
    
        

    def traverseList(self) :
        actualNode = self.head
        while actualNode is not None:
            print("%d " % actualNode.data,end=" ")
            actualNode = actualNode.nextNode


    def findmiddle(self):
        actualNode=self.head
        p=self.head
        q=self.head
        while p is not None:
            
            if p.nextNode is None:
                print("Middle element is: ",q.data)
                break
            elif p.nextNode.nextNode is None:
                print("Middle element is: ",q.data)
                break
            p=p.nextNode.nextNode
            q=q.nextNode
            

    

linkedlist1=LinkedList()

b=1
while(b):
    b=int(input("\nEnter choice\n 1 to insert \n 2 to traverse \n 3 to find middle \n 0 to exit: \n "))
    if b==1:
        a=int(input("Enter a number: "))
        linkedlist1.insertEnd(a)
    elif b==2:
        linkedlist1.traverseList()
    elif b==3:
        linkedlist1.findmiddle()





