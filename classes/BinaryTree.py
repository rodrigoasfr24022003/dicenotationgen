class BinaryTree:

    def __init__(self, data=None, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right

    
    def getData(self):
        return self._data
    
    def setData(self, data):
        self._data = data
    
    data=property(getData, setData)

    def getLeft(self):
        return self._left
    
    def setLeft(self, left):
        self._left = left
    
    left=property(getLeft, setLeft)

    def getRight(self):
        return self._right
    
    def setRight(self, right):
        self._right = right
    
    right=property(getRight, setRight)

    def __str__(self):
        if self.left is None and self.right is None:
            return str(self.data)
        
        left_str = str(self.left) if self.left else ""
        right_str = str(self.right) if self.right else ""

        return f"({left_str}{self.data}{right_str})"