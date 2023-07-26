class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node:
            result += str(temp_node.data)
            if temp_node:
                result += '->'
            temp_node = temp_node.next
        return result

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert(self, index, data):
        new_node = Node(data)
        # if index < 0 or index > self.length:
        #     return False
        # elif self.length == 0:
        #     self.head = new_node
        #     self.tail = new_node
        # elif index == 0:
        #     new_node.next = self.head
        #     self.head = new_node
        # else:
        temp_node = self.head
        for _ in range(index - 1):
            temp_node = temp_node.next
        new_node.next = temp_node.next
        temp_node.next = new_node

    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def search(self,target):
        current = self.head
        index = 0
        while current:
            if current.data == target:
                return index
            current = current.next
            index += 1
        return -1

    def get(self,index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def set_value(self, index, data):
        temp = self.get(index)
        if temp:
            temp.data = data
            return True
        return False

    def pop_first(self):
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        return popped_node

    def pop(self):
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        return popped_node

    def delete(self):
        self.head = self.tail = None


    def remove(self, index):

        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        return popped_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def remove_duplicate(self):
        if self.head is None:
            return
        node_data = set()
        current_node = self.head
        node_data.add(current_node.data)
        while current_node.next:
            if current_node.next.data in node_data:
                current_node.next = current_node.next.next
                self.length -= 1
            else:
                node_data.add(current_node.next.data)
                current_node = current_node.next
        self.tail = current_node




ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
ll.append(60)
ll.append(20)
ll.append(40)
print(ll)
print(ll.remove_duplicate())
print(ll)

