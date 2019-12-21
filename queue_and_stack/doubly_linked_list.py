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
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        if not self.head:
            return
        else:
            oldHead = self.head
            newHead = self.head.next
            newHead.prev = None
            oldHead.next = None
            self.head = newHead
            self.length -= 1
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
        if not self.tail:
            return
        else:
            self.length -= 1
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                oldTail = self.tail
                newTail = self.tail.prev
                oldTail.prev = None
                newTail.next = None
                self.tail = newTail

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if node == self.head:
            return
        if node == self.tail:
            self.remove_from_tail()
            self.add_to_head(node.value)
        else:
            val = node.value
            prevNode = node.prev
            nextNode = node.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            self.add_to_head(val)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if node = self.tail:
            return
        if node = self.head:
            self.remove_from_head()
            self.add_to_tail(node.value)
        else:
            val = node.value
            prevNode = node.prev
            nextNode = node.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            self.add_to_tail(val)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        pass

    """Returns the highest value currently in the list"""

    def get_max(self):
        pass
