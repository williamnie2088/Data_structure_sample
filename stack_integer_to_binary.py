"""
Use a stack data structure to convert integer values to binary

Example: 242

242 / 2 = 121 -> 0 (remainder)
121 / 2 = 60  -> 1 (remainder)
60 / 2 = 30   -> 0
30 / 2 = 15   -> 0
15 / 2 = 7    -> 1
7 / 2 = 3     -> 1
3 / 2 = 1     -> 1
1 / 2 = 0     -> 1


"""
from stack_data_structure import Stack

def div_by_2(dec_num):
    s = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num

num = div_by_2(242)
print(num[:: -1])

