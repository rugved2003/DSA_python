class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def push(self,data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
    
    def print_list(self):
        newnode = self.head
        while newnode is not None:
            print(newnode.data, end="->")
            newnode = newnode.next
        print("NULL")
        
    def printMiddle(self):
        elements = []
        newnode = self.head
        while newnode is not None:
            elements.append(newnode.data)
            newnode = newnode.next
        return elements[len(elements) // 2 ]
        
llist = LinkedList()
llist.push(1)
llist.push(20)
llist.push(101)
llist.push(15)
llist.push(35)
#llist.push(65)
llist.print_list()
Middle = llist.printMiddle()     
print(Middle)
    
