class Stack:
    def __init__(self, size = 16):
        self.stack = list()
        self.size = size
        self.top = -1
    def setSize(self, size):
        self.size = size
    def isEmpty(self):
        return self.top == -1
    def isFull(self):
        return self.top + 1 == self.size
    def top(self):
        if self.isEmpty():
            raise Exception('StackIsEmpty')
        else:
            return self.stack[stack.top]
    def push(self, obj):
        if self.isFull():
            raise Exception("StackOverFlow")
        else:
            self.stack.append(obj)
            self.top += 1
    def pop(self):
        if self.isEmpty():
            raise Exception('StackIsEmpty')
        else:
            self.top -= -1
            return self.stack.pop()
    def show(self):
        print(self.stack)

s = Stack()
print(s.isEmpty())
s.push(4)
s.push('dog')
s.push(True)
print(s.size)
print(s.isEmpty())
s.push(8.4)
s.show()
print(s.pop())
print(s.pop())
print(s.size)
