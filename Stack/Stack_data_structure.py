"""
Stack Data Structure
"""

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def get_stack(self):
        return self.items

s = Stack()
s.push('Hello World!')
s.push('This is your first stack function')
ptint(s.get_stack())