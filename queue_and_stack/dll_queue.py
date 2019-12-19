# import sys
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()  # instantiate an empty dll

    def enqueue(self, value):
        # call method from dll and pass in new value
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size > 0:  # if the list is not empty
            self.size -= 1
            return self.storage.remove_from_head()  # call method from dll
        else:
            return None

    def len(self):
        return self.size
