class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class Linked_List:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        ''' Creates a Node from provided data and inserts it into the sorted LL. '''
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        if self.is_new_node_higher_rank(current, new_node):
            new_node.set_next(current)
            self.head = new_node
            return
        while True:
            if not current.next_node:
                current.set_next(new_node)
                break
            if self.is_new_node_higher_rank(current.next_node, new_node):
                new_node.set_next(current.next_node)
                current.set_next(new_node)
                break
            else:
                current = current.next_node

    def is_new_node_higher_rank(self, current, new_node):
        ''' Compares letter rank and year rank. '''
        if self.get_letter_rank(new_node) > self.get_letter_rank(current):
            return True
        if self.get_letter_rank(new_node) == self.get_letter_rank(current):
            if self.get_year_rank(new_node) >= self.get_year_rank(current):
                return True
        return False

    def get_letter_rank(self, node):
        ''' Function to assign letter rank values. '''
        letter_rank = node.data.get('rank')[0]
        return {
            'A': 5,
            'B': 4,
            'C': 3,
            'D': 2,
            'E': 1,
            'U': 0
        }[letter_rank]

    def get_year_rank(self, node):
        ''' Returns year only rank. '''
        return node.data.get('rank')[1:]
