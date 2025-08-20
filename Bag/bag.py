from Linked_lists.singly_linked_list import SinglyLinkedList

class Bag:
    def __init__(self):
        self._data = SinglyLinkedList()
    
    def insert(self, value):
        self._data.insert_in_front(value)
    
    def traverse(self):
        self._data.traverse()

    