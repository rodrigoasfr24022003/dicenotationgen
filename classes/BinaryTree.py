class BinaryTree:

    def __init__(self, data=None, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def setData(self, data):
        self._data = data
    
    @property
    def left(self):
        return self._left
    
    @left.setter
    def setLeft(self, left):
        self._left = left
    
    @property
    def right(self):
        return self._left
    
    @right.setter
    def setLeft(self, right):
        self._right = right