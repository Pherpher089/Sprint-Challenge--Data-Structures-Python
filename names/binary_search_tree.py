# from dll_stack import Stack
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value == None:
            return
        elif self.value == None:
            self.value = BinarySearchTree(value)
        elif value >= self.value:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        else:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif self.right == None or self.left == None:
            return False
        else:
            if self.right.contains(target) or self.left.contains(target):
                return True

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if(self.right != None):
            self.right.for_each(cb)
        if(self.left != None):
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self == None:
            return
        if self.left != None:
            self.left.in_order_print(node)
        print(self.value)
        if self.right != None:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while queue.len() > 0:
            root = queue.dequeue()
            print(root.value)
            if root.left != None:
                queue.enqueue(root.left)
            if root.right != None:
                queue.enqueue(root.right)

    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.len() > 0:
            root = stack.pop()
            print(root.value)
            if root.left != None:
                stack.push(root.left)
            if root.right != None:
                stack.push(root.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node == None:
            return
        print(node.value)
        if node.left != None:
            node.left.pre_order_dft(node.left)
        if self.right != None:
            node.right.pre_order_dft(node.right)

    # Print Post-order recursive DFT

    def post_order_dft(self, node):
        if node == None:
            return
        if node.left != None:
            node.left.post_order_dft(node.left)
        if self.right != None:
            node.right.post_order_dft(node.right)
        print(node.value)


my_bst = BinarySearchTree(1)
my_bst.insert(8)
my_bst.insert(5)
my_bst.insert(7)
my_bst.insert(6)
my_bst.insert(3)
my_bst.insert(4)
my_bst.insert(2)
my_bst.pre_order_dft(my_bst)
