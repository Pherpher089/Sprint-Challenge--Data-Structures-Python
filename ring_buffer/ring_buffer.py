from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.oldest_entry = None

    def append(self, item):
        # Return if there is no data
        if item == None:
            return
        # If we have not met capacity
        if self.storage.length < self.capacity:
            self.storage.add_to_head(item)
            if self.storage.length == 1:
                self.oldest_entry = self.storage.head
        else:
            self.oldest_entry.value = item
            if self.oldest_entry == self.storage.head:
                self.oldest_entry = self.storage.tail
            else:
                self.oldest_entry = self.oldest_entry.prev

    def get(self):
        # Note: This is the only [] allowed
        list_buffer_contents = []
        node = self.storage.tail

        while node != None:
            list_buffer_contents.append(node.value)
            node = node.prev

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
