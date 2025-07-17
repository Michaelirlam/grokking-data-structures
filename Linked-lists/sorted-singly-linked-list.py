class SortedSinglyLinkedList:

    class Node:
        def __init__(self, data, next_node=None):
            self._data = data
            self._next = next_node

        def data(self):
            """gets the data stored in this node"""
            return self._data
        
        def next(self):
            """returns the successor of the current node"""
            return self._next
        
        def has_next(self):
            """Check if the node has a successor"""
            return self._next is not None
        
        def append(self, next_node):
            """Append a node to the current one"""
            self._next = next_node
    
    def __init__(self):
        """Initialise a new empty SinglyLinkedList object"""
        self._head = None

    def insert_in_sorted(self, data):
        current = self._head
        previous = None
        while current is not None:
            if current.data >= data:
                if previous is not None:
                    self._head = SortedSinglyLinkedList.Node(data, current)
                else:
                    previous.append(SortedSinglyLinkedList.Node(data, current))   
                    return
                previous = current
                current = current.next()  
        if previous is None:
            self._head = SortedSinglyLinkedList.Node(data)
        else:
            previous.append(SortedSinglyLinkedList.Node(data, None))
    
    def _search(self, target):
        """Private search method to find and return target node"""
        current = self._head
        while current is not None:
            if current.data() == target:
                return current
            current = current.next()
        return None
    
    def delete(self, target):
        """Deletes the first node with the target data"""
        current = self._head
        previous = None
        while current is not None:
            if current.data == target:
                if previous is None:
                    self._head = current.next()
                else:
                    previous.append(current.next())
                    return
            previous = current
            current = current.next()
        raise(ValueError(f"No element with value {target} was found in the list."))
    
    def delete_from_front(self):
        """Deletes the head of the list"""
        old_head = self._head
        if old_head is not None:
            self._head = old_head.next()
            return old_head.data
        return None
    
    def traverse(self, func):
        """Traverse the linked list and apply a function to each node's data."""
        result = []
        current = self._head
        while current is not None:
            result.append(func(current.data))
            current = current.next()
        return result