class Dice:
    
    def __init__(self, sides:int|list=6):
        if sides.isinstance(int):
            self._sides = list(range(1,sides+1))
        else:
            self._sides = sides
    
    @property
    def sides(self):
        return self._sides
    
    @sides.setter
    def sides(self, sides:list|int=6):
        if sides.isinstance(int):
            self._sides = list(range(1,sides+1))
        else:
            self._sides = sides