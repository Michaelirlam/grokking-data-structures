from core import Array

class DynamicUnsortedArray:
    def __init__(self, initial_capacity=1, typecode="i"):
        self._array = Array(initial_capacity, typecode)
        self._capacity = initial_capacity
        self._size = 0
        self._typecode = typecode
    
    def _double_size(self):
        """creates a new array that is double the capacity of the current and moves all elements over"""
        old_array = self._array
        self._array = Array(self._capacity * 2, self._typecode)
        self._capacity *= 2
        for i in range(self._size):
            self._array[i] = old_array[i]
    
    def _half_size(self):
        """Creates a new array that is half the size of the existing array"""
        old_array = self._array
        self._array = Array(self._capacity / 2, self._typecode)
        self._capacity /= 2
        for i in range(self._size):
            self._array[i] = old_array[i]

    def insert(self, value):
        """inserts new value into array"""
        # checks if current size is equal or greater than capacity and doubles capacity if True.
        if self._size >= self._capacity:
            self._double_size()
        self._array[self._size] = value
        self._size += 1

    def find(self, target):
        """Finds index of target"""
        for index in range(self._size):
            if self._array[index] == target:
                return index
        return None
    
    def delete(self, target):
        """Deletes target from array and reduces array size if at quarter capacity"""
        index = self.find(target)
        if index is None:
            raise(ValueError(f"Unable to delete element {target}: the entry is not in the array"))
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
        self._size -= 1
        if self._capacity > 1 and self._size <= self._capacity / 4:
            self._half_size()

    def delete_by_index(self, index):
        del self._array[index]
    
    