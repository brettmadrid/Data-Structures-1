# import sys
# sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if the new node's value is less than our current node's value
        # if so, it should be inserted on the left side
        if value < self.value:
            # if there's no left child here already
            # create new node and insert on the left
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                # otherwise if there is already a left child
                # repeat the process until no self.left can be found
                self.left.insert(value)

        # check if the new node's value is >= to our current node's value
        # if so, it should be inserted on the right side
        elif value >= self.value:
            # if there's no right child here already
            # create new node and insert on the right
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                # otherwise if there is already a right child
                # repeat the process until no self.right can be found
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # if the value of the current node equals the target value
        # we have found a match - return True
        if self.value == target:
            return True

        # if the target value is less than the value of the current node
        if target < self.value:
            # if the current node does not have a left child
            if not self.left:
                return False
            else:
                # otherwise, repeat process for current node's left child
                return self.left.contains(target)
        else:  # if the value is greater than the current node's value
            # do the same for the right side
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BinarySearchTree(5)
bst.insert(2)
bst.insert(3)
bst.insert(7)
bst.insert(6)
print(bst.contains(5))
print(bst.contains(2))
print(bst.contains(3))
print(bst.contains(7))
print(bst.contains(6))
