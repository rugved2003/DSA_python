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
        
    def palindrome(self):
        elements = []
        newnode = self.head
        while newnode is not None:
            elements.append(newnode.data)
            newnode = newnode.next
        return elements == elements[::-1]
llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(3)
llist.push(2)
llist.push(1)
llist.print_list()
palindrome = llist.palindrome()
print(palindrome)

    
