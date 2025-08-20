class Node:
    def __init__(self, data, next_node=None):
        self._data = data
        self._next = next_node

    def data(self):
        return self._data
    
    def next(self):
        return self._next
    
    def has_next(self):
        return self._next is not None
    
    def append(self, next_node):
        self._next = next_node