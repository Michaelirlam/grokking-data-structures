from core import Array

class DynamicSortedArray:
    def __init__(self, initial_capacity, typecode="i"):
        self._array = Array(initial_capacity, typecode)
        self._capacity = initial_capacity
        self._size = 0
        self._typecode = typecode

    def _double_size(self):
        old_array = self._array
        self._array = Array(self._capacity * 2, self._typecode)
        self._capacity *= 2
        for i in range(self._size):
            self._array[i] = old_array[i]
    
    def _half_size(self):
        old_array = self._array
        self._array = Array(self._capacity / 2, self._typecode)
        self._capacity /= 2
        for i in range(self._size):
            self._array[i] = old_array[i]
    
    def insert(self, value):
        if self._size >= self._capacity:
            self._double_size()
        for i in range(self._size, 0, -1):
            if self._array[i -1] <= value:
                self._array[i] = value
                self._size += 1
                return
            else:
                self._array[i] = self._array[i-1]
        self._array[0] = value
        self._size +=1

    def find(self, target):
        for index in range(self._size):
            if self._array[index] == target:
                return index
        return None
    
    def delete(self, target):
        index = self.find(target)
        if index is None:
            raise(ValueError(f"Unable to delete element {target}: the entry is not in the array"))
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
        self._size -= 1
        if self._capacity > 1 and self._size <= self._capacity / 4:
            self._half_size()