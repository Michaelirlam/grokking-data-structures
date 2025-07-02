import array

class UnsortedArray:
    def __init__(self, max_size, typecode = "1"):
        self._array = array(max_size, typecode)
        self._max_size = max_size
        self._size = 0

    def insert(self, new_entry):
        if self._size >= len(self._array):
            raise ValueError("The array is already full")
        else:
            self._array[self._size] = new_entry
            self._size += 1

    def delete(self, index):
        if self._size == 0:
            raise ValueError("You cannot delete, the array is empty.")
        elif index < 0 or index >= self._size:
            raise ValueError(f"Index {index} is out of range.")
        else:
            self._array[index] = self._array[self._size - 1]
            self._size -= 1
        
    def search(self, target):
        for index in range(0, self._size):
            if self._array[index] == target:
                return index
            else:
                return None
    
    def traverse(self, callback):
        for index in range(0, self._size):
            callback(self._array[index])

    def max_in_array(self):
        if len(self._array) == 0:
            raise Exception("Max of an empty array")
        max_index = 0
        for index in range(1, len(self._array)):
            if self._array[index] > self._array[max_index]:
                max_index = index
        return max_index, self._array[max_index]
    
    def min_in_array(self):
        if len(self._array) == 0:
            raise Exception("Min of an empty array")
        min_index = 0
        for index in range(1, len(self._array)):
            if self._array[index] < self._array[min_index]:
                min_index = index
        return min_index, self._array[min_index]

    def max_and_min_array(self):
        return f"Max: {self.max_in_array()}, Min: {self.min_in_array()}"