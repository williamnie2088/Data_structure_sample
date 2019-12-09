class Stack():
    def __init__ (self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []


def reverse_string(stack, input_str):
    for i in range (len(input_str)):
        stack.push(input_str[i])


    rev_str = ""
    
    while not stack.is_empty():
        rev_str += stack.pop()
    return rev_str

stack = Stack()
string = input("Enter the string you want to enter: ")

input_str = string
print(reverse_string(stack, input_str))


easier = "revert"
print(easier[:: -1])
