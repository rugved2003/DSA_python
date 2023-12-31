class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values=[str(x) for x in self.items]
        values = reversed(values)
        return ' '.join(values)

    def isEmpty(self):
        if not self.items:
            return True
        else:
            return False

    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted at the end of Queue"

    def dequeue(self):
        if self.isEmpty():
            return "No elements"
        else:
            return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return "No element"
        else:
            return  self.items[0]

    def delete(self):
        self.items = None


customQueue = Queue()
print(customQueue.isEmpty())
customQueue.enqueue(10)
customQueue.enqueue(20)
customQueue.enqueue(30)
print(customQueue)
customQueue.dequeue()
print(customQueue)
print("-----")

print(customQueue.peek())
customQueue.delete()
print(customQueue.isEmpty())
print(customQueue.peek())



