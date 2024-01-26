import ctypes
class DynamicArray:
    def __init__(self):
        self._n = 0 
        self._capacity = 1
        self._A = self.make_array(self._capacity)

    def __len__(self):
        return self._n
    
    def get_item(self, index):
        if not 0 < index < self._n:
            raise IndexError
        return self._A[index]
    
    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2*self._capacity)
            self._A[self._n] = obj
            self._n += 1

    def _resize(self, c):
        B = self.make_array(c)
        for k in range (self._n):
            B[k] = self._A[k]
        
        self._A = B
        self._capacity = c

    def make_array(self, c):
        return (c*ctypes.py_object)()
    

