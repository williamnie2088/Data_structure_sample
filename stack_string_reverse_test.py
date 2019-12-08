class Stack():
    def __init__(object):
        object.items = []
    def push(object, item):
        object.items.append(item)
    def pop(object):
        return object.items.pop()
    def is_empty(object):
        return object.items == []

def revert(stack, input_str):
    for i in range (len(input_str)):
        stack.push(input_str[i])
    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()
    return rev_str

stack = Stack()

input_word = input("Enter the word to reverse: ")
input_str = input_word

print(revert(stack, input_str))
