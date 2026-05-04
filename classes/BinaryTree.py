from classes.BinaryTree import BinaryTree
class BinaryTree:

    def __init__(self, data, left:BinaryTree|None=None, right:BinaryTree|None=None):
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
    def setLeft(self, left:BinaryTree|None=None):
        self._left = left
    
    @property
    def right(self):
        return self._left
    
    @right.setter
    def setLeft(self, right:BinaryTree|None=None):
        self._right = right