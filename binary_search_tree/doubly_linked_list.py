"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers 
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        # this is the first element in the list
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        if not self.head:
            return
        else:
            oldHead = self.head
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            else:
                newHead = oldHead.next
                newHead.prev = None
                oldHead.next = None
                self.head = newHead
            return oldHead.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        newTail = ListNode(value)
        self.length += 1
        if not self.tail:
            self.head = newTail
            self.tail = newTail
        else:
            self.tail.next = newTail
            newTail.prev = self.tail
            self.tail = newTail

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if node is self.head:
            return
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if node == self.tail:
            return
        if node == self.head:
            self.remove_from_head()
            self.add_to_tail(node.value)
        else:
            val = node.value
            self.delete(node)
            prevNode = node.prev
            nextNode = node.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            self.add_to_tail(val)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        if not self.head and not self.tail:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        elif self.head == node:
            self.head = node.next
            self.length -= 1
            node.delete()
        elif self.tail == node:
            self.tail = node.prev
            self.length -= 1
            node.delete()
        else:
            self.length -= 1
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        currNode = self.head
        maxValue = self.head.value
        while currNode:
            if currNode.value > maxValue:
                maxValue = currNode.value
            currNode = currNode.next
        return maxValue


'''
    Gets middle value in a linked list
'''


def get_middle(linked_list):
    slow_pointer = linked_list.head
    fast_pointer = linked_list.head
    while fast_pointer is not None:
        fast_pointer = fast_pointer.next
        if fast_pointer is not None:
            fast_pointer = fast_pointer.next
            slow_pointer = slow_pointer.next
    return slow_pointer.value


'''
    Reverses a linked list
'''


def reverse_list(linked_list):
    curr = linked_list.head
    new = curr.next
    # this is new tail
    curr.next = None
    prev = None

    while new is not None:
        prev = curr
        curr = new
        new = curr.next
        curr.next = prev
        linked_list.head = curr