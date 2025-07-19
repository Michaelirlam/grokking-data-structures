class DoublyLinkedList:

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

    def insert_in_front(self, data):
        if self._head is None:
            self._tail = self._head = DoublyLinkedList.Node(data)
        else:
            old_head = self._head
            self._head = DoublyLinkedList.Node(data)
            self._head.append(old_head)
    
    def insert_to_back(self, data):
        if self._tail is None:
            self._tail = self._head = DoublyLinkedList.Node(data)
        else:
            old_tail = self._tail
            self._tail = DoublyLinkedList.Node(data)
            self._tail.prepend(old_tail)
    
    def insert_in_middle(self, data, target):
        current = self._head
        new_node = DoublyLinkedList.Node(data)
        while current is not None:
            if current.data() == target:
                next_node = current.next()
                
                current._next = new_node
                new_node._prev = current
                new_node._next = next_node
                
                if next_node:
                    next_node._prev = new_node
                else:
                    self._tail = new_node  # if we inserted at the end, update tail
                
                return
            current = current.next()
                