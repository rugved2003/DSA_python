class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def createSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "CSLL hac been created"

    def insert(self, value, location):
        if self.head is None:
            return 'The head refernce is None'
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode

            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode

            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

            return "The node has beenm sucessfully inserted"

    # traversal

    def traversal(self):
        if self.head is None:
            print("there is no any element for traversal")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    # searching
    def search(self, nodeValue):
        if self.head is None:
            return "no element"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "the node doesn't exist"


    #delete
    def delete(self, location):
        if self.head is None:
            return "no element"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def deleteall(self):
        self.head = None
        self.tail.next = None
        self.tail = None





circularSLL = CircularSinglyLinkedList()
print(circularSLL.createSLL(1))
circularSLL.insert(0, 0)
circularSLL.insert(2, 1)
circularSLL.insert(3, 1)
circularSLL.insert(2, 2)
print([node.value for node in circularSLL])
# circularSLL.traversal()
circularSLL.delete(0)
print([node.value for node in circularSLL])
circularSLL.deleteall()
print([node.value for node in circularSLL])


