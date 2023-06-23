class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def push(self,newdata):
        newnode = Node(newdata)
        newnode.next = self.head
        self.head = newnode
        
    def getcount(self):
        last = self.head
        count = 0
        while(last):
            count+=1
            last = last.next
        return count
        
list = Linkedlist()
list.push(10)
list.push(2)
list.push(6)
print(list.getcount())
