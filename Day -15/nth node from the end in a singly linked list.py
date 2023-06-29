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
        
    def Nodefromend(self,n):
        elements = []
        newnode = self.head
        while newnode is not None:
            elements.append(newnode.data)
            newnode = newnode.next
        e = elements[::-1]
        return e[n-1]
    
llist = LinkedList()
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
llist.print_list()
n = int(input("Enter nth node from the end: "))
Noden = llist.Nodefromend(n)     
print(Noden)