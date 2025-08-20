class CircularSinglyLinkedList:

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
    
    def insert_to_back(self, data):
        """Inserts new node at the tail of the list"""
        new_node = CircularSinglyLinkedList.Node(data)

        if self._head is None:
            new_node.append(new_node)
            self._head = new_node
        else:
            current = self._head
            while current.next() != self._head:
                current = current.next()
            current.append(new_node)
            new_node.append(self._head)
    
    def insert_in_front(self, data):
        """Insert new node at the front of the list"""
        new_node = CircularSinglyLinkedList.Node(data)

        if self._head is None:
            new_node.append(new_node)
            self._head = new_node
        else:
            current = self._head

            while current.next() != self._head:
                current = current.next()
            current.append(new_node)
            new_node.append(self._head)
            self._head = new_node
    
    def _search(self, target):
        """Private search method to find and return target node"""
        if self._head is None:
            return None

        current = self._head
        while True:
            if current.data() == target:
                return current
            current = current.next()
            if current == self._head:
                break 
        return None
    
    def delete(self, target):
        """Deletes the first node with the target data"""
        if self._head is None:
            raise ValueError("List is empty.")

        # If deleteing the head node
        if self._head.data() == target:
            if self._head.next() == self._head:
                self._head = None
            else:
                current = self._head
                while current.next() != self._head:
                    current = current.next()
                new_head = self._head.next()
                current.append(new_head)
                self._head = new_head
            return

        # If deleting a non-head node
        previous = self._head
        current = self._head.next()

        while current != self._head:
            if current.data() == target:
                previous.append(current.next())
                return
            previous = current
            current = current.next()

        # If not found after full circle
        raise ValueError(f"No element with value {target} was found in the list.")
    
    def traverse(self, func):
        """Traverse the list and apply a function to each node's data."""
        result = []
        current = self._head
        while True:
            result.append(func(current.data()))
            current = current.next()
            if current is self._head:
                break
        return result
