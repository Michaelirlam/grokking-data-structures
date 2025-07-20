class SortedDoublyLinkedList:

    class Node:
        def __init__(self, data):
            self._data = data
            self._prev = None
            self._next = None
        
        def data(self):
            return self._data
        
        def next(self):
            return self._next
        
        def has_next(self):
            return self._next is not None
        
        def append(self, next_node):
            self._next = next_node
            if next_node is not None:
                next_node._prev = self
        
        def prev(self):
            return self._prev
        
        def has_prev(self):
            return self._prev is not None

        def prepend(self, prev_node):
            self._prev = prev_node
            if prev_node is not None:
                prev_node._next = self
    
    def __init__(self):
        self._head = None
        self._tail = None
    
    def sorted_insert(self, data):
        new_node = SortedDoublyLinkedList.Node(data)

        if self._head is None:
            self._head = self._tail = new_node
            return
        current = self._head

        while current is not None and current.data() < data:
            current = current.next()
        if current is None:
            # Insert at end
            self._tail.append(new_node)
            self._tail = new_node
        elif current.prev() is None:
            # Insert at beginning
            new_node.append(current)
            self._head = new_node
        else:
            # Insert in the middle
            prev_node = current.prev()
            prev_node.append(new_node)
            new_node.append(current)
    
    def _search(self, target):
        """Private search method to find and return target node"""
        current = self._head
        while current is not None:
            if current.data() == target:
                return current
            current = current.next()
        return None
    
    def traverse(self, func):
        """Traverse the linked list and apply a function to each node's data."""
        result = []
        current = self._head
        while current is not None:
            result.append(func(current.data()))
            current = current.next()
        return result

    def reverse_traverse(self, func):
        """Traverse list in reverse order and apply a function to each node's data"""
        result = []
        current = self._tail
        while current is not None:
            result.append(func(current.data()))
            current = current.prev()
        return result

    def delete(self, target):
        """Delete target node and update predecessor and successort links"""
        node = self._search(target)
        if node is None:
            raise(ValueError(f"{target} not found in the list."))
        if node.prev() is None:
            self._head = node.next()
            if self._head is None:
                self._tail = None
            else:
                self._head.prepend(None)
        elif node.next() is None:
            self._tail = node.prev()
            self._tail.append(None)
        else:
            node.prev().append(node.next())
            del node