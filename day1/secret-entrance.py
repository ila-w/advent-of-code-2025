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
def get_rotated(input):
    result = 0

    instructions = "".split(input)
    
    dial = DoublyCircularLinkedList()
    for i in range(100):
        dial.append(i)


    for item in instructions:
        direction = item[0]
        amount = item[1:]

        






    return result

# default input given from problem statement
input = "L68 L30 R48 L5 R60 L55 L1 L99 R14 L82"



# print results
print(get_rotated(input))
