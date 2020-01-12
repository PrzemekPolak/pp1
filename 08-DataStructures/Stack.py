class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if self.is_empty():
            return None
        print(f'Pobierz: {self.stack[len(self.stack)-1]}')
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def is_empty(self):
        return len(self.stack)==0


stos = Stack()
stos.push(1)
stos.push(2)
stos.pop()
stos.push(3)
stos.push(4)
stos.push(5)
stos.pop()
stos.pop()