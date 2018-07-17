class Stack:
    temp = 5
    def __init__(self):
        self.tos = -1
        self.arr = []

    def push(self,  x):
        self.tos = self.tos + 1
        self.arr.append(x)

    def pop(self):
        self.arr.remove(self.arr[self.tos])
        self.tos = self.tos - 1

    def print(self):
        print(self.arr)



stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.pop()
stack.print()