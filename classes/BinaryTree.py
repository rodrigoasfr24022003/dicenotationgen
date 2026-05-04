class BinaryTree:

    def __init__(self, data=None, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right

    
    def data(self):
        return self._data
    
    def setData(self, data):
        self._data = data
    
    data=property(data, setData)

    def left(self):
        return self._left
    
    def setLeft(self, left):
        self._left = left
    
    left=property(left, setLeft)

    def right(self):
        return self._left
    
    def setRight(self, right):
        self._right = right
    
    right=property(right, setRight)