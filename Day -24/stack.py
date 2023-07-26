
class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    #isempty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def ifFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
    #push
    def push(self,value):
        self.list.append(value)
        return "element has been successfully inserted"

    def pop(self):
        if self.isEmpty():
            return "there is not any element in the stack"
        else:
            return self.list.pop()

    #peek
    def peek(self):
        if self.isEmpty():
            return "there is not any element in the stack"
        else:
            return self.list[len(self.list)-1]

    def delete(self):
        self.list = None


customStack = Stack()
print(customStack.isEmpty())
customStack.push(10)
customStack.push(20)
customStack.push(30)
print(customStack)
print("*****")
print(customStack.pop())
print("*****")
print(customStack)
print(customStack.peek())
customStack.delete()
print(customStack.isEmpty())
