"""
Stack data structure
"""

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self,item):
        return self.items.pop(item)

    def get_stack(self):
        return self.items

s = Stack()
s.push("Hello world!")
s.push("This if your first stack function.")
print(s.get_stack())

s.pop(0)
print("after removing hello world", s.get_stack())
