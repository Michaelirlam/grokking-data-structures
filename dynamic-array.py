from core import Array

class DynamicArray:
    def __init__(self, initial_capacity=1, typecode="i"):
        self._array = Array(initial_capacity, typecode)
        self._capacity = initial_capacity
        self._size = 0
        self._typecode = typecode