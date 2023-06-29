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
        
    def deleteAlt(self):
        current = self.head
        
        while current and current.next:
            current.next = current.next.next
            current = current.next
    
llist = LinkedList()
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
llist.print_list()

llist.deleteAlt()
llist.print_list()
