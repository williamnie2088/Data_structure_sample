"""
Stack data structure
"""

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def get_stack(self):
        return self.items

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def clear(self):
        return self.items.clear()


#s = Stack()
#s.push("Hello world!")
#s.push("This if your first stack function.")
#s.push("Testing with more lines")
#print("originally, we have the following items in the list: ", s.get_stack())

#s.pop()
#print("\nAfter poping 0", s.get_stack())

#print("\nTake a peek on the last item: ", s.peek())

#s.clear()
#print("\nAfter clearing the list: ", s.is_empty())
