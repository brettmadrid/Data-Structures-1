# import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # faster than an array at insertion and deletions
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)  # call dll method and pass in value
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()  # call dll method

    def len(self):
        return self.size
