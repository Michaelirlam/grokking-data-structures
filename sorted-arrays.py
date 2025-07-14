from core import Array

class SortedArray:
    def __init__(self, max_size, typecode="i"):
        self._array = Array(max_size, typecode)
        self._max_size = max_size
        self._size = 0

    def insert(self, value):
        if self._size >= self._max_size:
            raise ValueError(f"Array is already full, max size: {self._max_size}")
        else:
            for i in range(self._size, 0, -1):
                if self._array[i - 1] <= value:
                    self._array[i] = value
                    self._size += 1
                    return
                else:
                    self._array[i] = self._array[i-1]
            self._array[0] = value
            self._size += 1

    def linear_search(self, target):
        for index in range(self._size):
            if self._array[index] == target:
                return index
            elif self._array[index] > target:
                return None
        return None
    
    def binary_search(self, target):
        left = 0
        right = self._size - 1
        while left <= right:
            mid_index = (left + right) // 2
            mid_value = self._array[mid_index]
            if mid_value == target:
                return mid_index
            elif mid_value > target:
                right = mid_index - 1
            else:
                left = mid_index + 1
        return None
    
    def binary_search_first(self, target):
        left = 0
        right = self._size - 1
        result = None
        while left <= right:
            mid_index = (left + right) // 2
            mid_value = self._array[mid_index]
            if mid_value == target:
                result = mid_index
                right = mid_index - 1
            elif mid_value > target:
                right = mid_index - 1
            else:
                left = mid_index + 1
        return result
    
    def delete(self, target):
        index = self.linear_search(target)
        if index is None:
            raise ValueError(f"Unable to delete element {target}: the entry is not in the array")
        else:
            for i in range(index, self._size - 1):
                self._array[i] = self._array[i-1]
            self._size -= 1
    
    def delete_by_index(self, index):
        if index >= len(self._array):
            raise ValueError("Not a valid index.")
        else:
            for i in range(index, self._size - 1):
                self._array[i] = self._array[i-1]
            self._size -= 1
    
    def traverse(self, callback):
        for index in range(0, self._size):
            callback(self._array[index])

