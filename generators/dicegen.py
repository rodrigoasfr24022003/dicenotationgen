import random
sysr=random.SystemRandom()
def generateDice(min_sides:int,max_sides:int,customSides:bool=False,minCustomSideValue:int=0,maxCustomSideValue:int=0, allowSubExpressions:bool=False, allowNegativeValuesWithoutZero:bool=False):
    if not customSides:
        if max_sides < min_sides:
            min_sides_copy = min_sides
            min_sides = max_sides
            max_sides = min_sides_copy
        sides = sysr.randint(min_sides,max_sides)
        return ('d'+str(sides),sides)
    else:
        sideAmount = sysr.randint(min_sides,max_sides)
        sideDict = {i:str(i) for i in range(1,sideAmount+1)}
        for i in sideDict.keys():
            if not allowNegativeValuesWithoutZero:
                sideDict[i] = sysr.randint(minCustomSideValue, maxCustomSideValue)
            else:
                sideDict[i] = sysr.choice([sysr.randint(-maxCustomSideValue, -minCustomSideValue),sysr.randint(minCustomSideValue, maxCustomSideValue)])
        out = 'd'+str(sideAmount)
        out += ('V{')
        for i in sideDict.keys():
            out += (str(i)+":"+str(sideDict[i]))
        out += "}"
        return out