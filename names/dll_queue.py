from doubly_linked_list import DoublyLinkedList
import sys
# sys.path.append('../doubly_linked_list/')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            ret_val = self.storage.head.value
            self.storage.remove_from_head()
            self.size -= 1
            return ret_val

    def len(self):
        return self.size