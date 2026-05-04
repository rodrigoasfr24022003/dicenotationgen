from classes.Dice import Dice
class XdY:

    def __init__(self, x:int, y:Dice, keepHighest:int|None=None, keepLowest:int|None=None, keepMiddle:int|None=None, dropHighest:int|None=None, dropLowest:int|None=None, dropCondition:function|None=None, clampCondition:function|None=None, unique:bool=False, uniqueExclusions:function|None=None, explosiveCondition:function|None=None, explosionLimit:int=-1, inflate:bool=False, inflateType:str|None = None, reduce:bool=False, conditionsDisregardExplodedDice:bool=True, rerollCondition:function|None=None, rerollLimit:int=-1, countCondition:function|None=None, convertToString:str|None=None):
        self._x = x
        self._y = y
        self._keepHighest = keepHighest
        self._keepLowest = keepLowest
        self._keepMiddle = keepMiddle
        self._dropHighest = dropHighest
        self._dropLowest = dropLowest
        self._dropCondition = dropCondition
        self._clampCondition = clampCondition
        self._unique = unique
        self._uniqueExclusions = uniqueExclusions
        self._explosiveCondition = explosiveCondition
        if explosionLimit == -1 or explosionLimit >= 1:
            self._explosionLimit = explosionLimit
        else:
            self._explosionLimit = -1
        self._inflate = inflate
        if inflateType in ["Singles","Evens","DCC","Dice the Demiurge"] or inflateType == None:
            self._inflateType = inflateType
        else:
            self._inflateType = "Evens"
        self._reduce = reduce
        self._conditionsDisregardExplodedDice = conditionsDisregardExplodedDice
        self._rerollCondition = rerollCondition
        if rerollLimit == -1 or rerollLimit >= 1:
            self._rerollLimit = rerollLimit
        else:
            self._rerollLimit = -1
        self._countCondition = countCondition
        if convertToString in ["Normal", "Individual", "Full", "Full and Individual"] or convertToString == None:
            self._convertToString = convertToString
        else:
            self._convertToString = None
    
    
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    @property
    def keepHighest(self):
        return self._keepHighest
    @property
    def keepLowest(self):
        return self._keepLowest
    @property
    def keepMiddle(self):
        return self._keepMiddle
    @property
    def dropHighest(self):
        return self._dropHighest
    @property
    def dropLowest(self):
        return self._dropLowest
    @property
    def dropCondition(self):
        return self._dropCondition
    @property
    def clampCondition(self):
        return self._clampCondition
    @property
    def unique(self):
        return self._unique
    @property
    def uniqueExclusions(self):
        return self._uniqueExclusions
    @property
    def explosiveCondition(self):
        return self._explosiveCondition
    @property
    def explosionLimit(self):
        return self._explosionLimit
    @property
    def inflate(self):
        return self._inflate
    @property
    def inflateType(self):
        return self._inflateType
    @property
    def reduce(self):
        return self._reduce
    @property
    def conditionsDisregardExplodedDice(self):
        return self._conditionsDisregardExplodedDice
    @property
    def rerollCondition(self):
        return self._rerollCondition
    @property
    def rerollLimit(self):
        return self._rerollLimit
    @property
    def countCondition(self):
        return self._countCondition
    @property
    def convertToString(self):
        return self._convertToString
    
    x.setter
    def setX(self, x):
        self._x = x
    y.setter
    def setY(self, y):
        self._y = y
    keepHighest.setter
    def setKeepHighest(self, keepHighest):
        self._keepHighest = keepHighest
        self._keepLowest = None
        self._keepMiddle = None
        self._dropHighest = None
        self._dropLowest = None
        self._dropCondition = None
    keepLowest.setter
    def setKeepLowest(self, keepLowest):
        self._keepHighest = None
        self._keepLowest= keepLowest
        self._keepMiddle = None
        self._dropHighest = None
        self._dropLowest = None
        self._dropCondition = None
    keepMiddle.setter
    def setKeepMiddle(self, keepMiddle):
        self._keepHighest = None
        self._keepLowest= None
        self._keepMiddle = keepMiddle
        self._dropHighest = None
        self._dropLowest = None
        self._dropCondition = None
    dropHighest.setter
    def setDropHighest(self, dropHighest):
        self._keepHighest = None
        self._keepLowest= None
        self._keepMiddle = None
        self._dropHighest = dropHighest
        self._dropLowest = None
        self._dropCondition = None
    dropLowest.setter
    def setDropLowest(self, dropLowest):
        self._keepHighest = None
        self._keepLowest= None
        self._keepMiddle = None
        self._dropHighest = None
        self._dropLowest = dropLowest
        self._dropCondition = None
    dropCondition.setter
    def setDropCondition(self, dropCondition):
        self._keepHighest = None
        self._keepLowest= None
        self._keepMiddle = None
        self._dropHighest = None
        self._dropLowest = None
        self._dropCondition = dropCondition
    clampCondition.setter
    def setClampCondition(self, clampCondition):
        self._clampCondition = clampCondition
    unique.setter
    def setUnique(self, unique):
        self._unique = unique
    uniqueExclusions.setter
    def setUniqueExclusions(self, uniqueExclusions):
        self._uniqueExclusions = uniqueExclusions
    explosiveCondition.setter
    def setExplosiveCondition(self, explosiveCondition):
        self._explosiveCondition = explosiveCondition
    explosionLimit.setter
    def setExplosionLimit(self, explosionLimit):
        if explosionLimit == -1 or explosionLimit >= 1:
            self._explosionLimit = explosionLimit
        else:
            self._explosionLimit = -1
    inflate.setter
    def setInflate(self, inflate: bool):
        self._inflate = inflate
        self._inflateType = "Evens" if inflate else None
        self._reduce = False
    inflateType.setter
    def setInflateType(self, inflateType):
        if inflateType in ["Singles","Evens","DCC","Dice the Demiurge"] or inflateType == None:
            self._inflateType = inflateType
        else:
            self._inflateType = "Evens"
    reduce.setter
    def setReduce(self, reduce):
        self._inflate = False
        self._inflateType = None
        self._reduce = reduce
    conditionsDisregardExplodedDice.setter
    def setConditionsDisregardExplodedDice(self, conditionsDisregardExplodedDice):
        self._conditionsDisregardExplodedDice = conditionsDisregardExplodedDice
    rerollCondition.setter
    def setRerollCondition(self, rerollCondition):
        self._rerollCondition = rerollCondition
    rerollLimit.setter
    def setRerollCondition(self, rerollLimit):
        if rerollLimit == -1 or rerollLimit >= 1:
            self._rerollLimit = rerollLimit
        else:
            self._rerollLimit = -1
    countCondition.setter
    def countCondition(self, countCondition):
        self._countCondition = self.countCondition
    convertToString.setter
    def setConvertToString(self, convertToString):
        if convertToString in ["Normal", "Individual", "Full", "Full and Individual"] or convertToString == None:
            self._convertToString = convertToString
        else:
            self._convertToString = None