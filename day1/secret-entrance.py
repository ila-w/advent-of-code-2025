###############################################
##  Doubly Circular Linked List Construction ##
###############################################
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        new_node = Node(data)

        if not self.head:
            new_node.next = new_node.prev = new_node
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node

###############################################


# Processes the instructions given and returns 
# the resulting location.
def get_rotated_part_one(input, start):
    result = 0

    instructions = input.split()
    
    dial = DoublyCircularLinkedList()
    for i in range(100):
        dial.append(i)
    
    current = dial.head

    for i in range(start):
        current = current.next

    for item in instructions:
        direction = item[0]
        amount = int(item[1:])

        for i in range(amount):
            if direction == "L":
                current = current.prev
            else:
                current = current.next
        
        if current.data == 0:
            result += 1

    return result


# Processes the instructions given and returns 
# the resulting location.
def get_rotated_part_two(input, start):
    result = 0

    instructions = input.split()
    
    dial = DoublyCircularLinkedList()
    for i in range(100):
        dial.append(i)
    
    current = dial.head

    for i in range(start):
        current = current.next

    for item in instructions:
        direction = item[0]
        amount = int(item[1:])

        for i in range(amount):
            if current.data == 0:
                result += 1

            if direction == "L":
                current = current.prev
            else:
                current = current.next

    return result

# default input given from problem statement
input = "L68 L30 R48 L5 R60 L55 L1 L99 R14 L82"
start = 50

# Helps with parsing out the input file for my specific puzzle
#puzzle = ""
#with open("./day1/input.txt") as f:
#    file = f.read().splitlines()
#puzzle = " ".join(file)


# Prints out the results
print(get_rotated_part_one(input, start))
print(get_rotated_part_two(input, start))

# My specific puzzle method calls
#print(get_rotated_part_one(puzzle, start))
#print(get_rotated_part_two(puzzle, start))