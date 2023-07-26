class Node:
    def __init__(self, value = None):
        self.value  = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isempty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.isempty():
            return "No elements"
        else:
            nodevalue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodevalue

    def peek(self):
        if self.isempty():
            return "No elements"
        else:
            nodevalue = self.LinkedList.head.value
            return nodevalue
    def delete(self):
        self.LinkedList.head = None


customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print("-------")
customStack.pop()
print(customStack)
print("-------")
print(customStack.peek())
customStack.delete()
print(customStack.isempty())