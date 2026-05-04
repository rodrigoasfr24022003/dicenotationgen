from dicegen import generateDice
import random
sysr = random.SystemRandom()
def conditionHelper(maxConditions:int, min_sides:int, max_sides:int, allow_zero:bool=False, allowNegativeValues:bool=False):
    out = "D"
    conditionAmount = sysr.randint(1,min(max_sides,maxConditions))
    if conditionAmount == 1:
        condition = sysr.choice(["<",">",""])
        if condition == "<":
            conditionArgument = sysr.randint(2, max_sides)
        elif condition == ">":
            conditionArgument = sysr.randint(1, max_sides-1)
        elif condition == "":
            conditionArgument = sysr.randint(1, max_sides)
        diceString += "{" + condition + conditionArgument + "}"
    elif conditionAmount == 2:
        condition1 = sysr.choice(["<",">",""])
        if condition1 == "<":
            condition1Argument = sysr.randint(2, max_sides)
            condition2 = sysr.choice([">", ""])
            if condition2 == ">":
                condition2Argument = sysr.randint(condition1Argument, max_sides-1)
            else:
                condition2Argument = sysr.randint(condition1Argument, max_sides)
        elif condition1 == ">":
            condition1Argument = sysr.randint(1, max_sides-1)
            condition2 = sysr.choice(["<", ""])
            condition2Argument = sysr.randint(1,condition1Argument)
        elif condition1 == "":
            condition1Argument = sysr.randint(1, max_sides)
            condition2 = sysr.choice(["<",">",""])
            if condition2 == "<":
                condition2Argument = sysr.choice(list(range(2, max_sides)).remove(condition1Argument))
            if condition2 == ">":
                condition2Argument = sysr.choice(list(range(1, max_sides-1)).remove(condition1Argument))
            if condition2 == "":
                condition2Argument = sysr.choice(list(range(1, max_sides)).remove(condition1Argument))
        diceString += "{" + condition1 + condition1Argument + "," + condition2 + condition2Argument + "}"
    elif conditionAmount > 2:
        conditions = []
        for i in range(4):
            if i == 0:
                conditions.append(sysr.choice(["<",">",""]))
            elif i == 1:
                if conditions[0] == "<":
                    conditions.append(sysr.choice([">",""]))
                elif conditions[0] == ">":
                    conditions.append(sysr.choice(["<",""]))
                else:
                    conditions.append(sysr.choice(["<",">",""]))
            elif i > 1:
                if "<" in conditions and ">" in conditions:
                    conditions.append("")
                if "<" in conditions and ">" not in conditions:
                    conditions.append(sysr.choice([">",""]))
                if ">" in conditions and "<" not in conditions:
                    conditions.append(sysr.choice(["<",""]))
                if "<" not in conditions and ">" not in conditions:
                    conditions.append(sysr.choice(["<",">",""]))
        conditionArguments = [0,0,0,0]
        for i in range(len(conditions)):
            if "<" in conditions and ">" in conditions:
                if conditions.index("<") < conditions.index(">"):
                    if conditions[i] == "<":
                        conditionArguments[i] = sysr.randint(2, max_sides)
                    elif conditions[i] == ">":
                        conditionArguments[i] = sysr.randint(conditionArguments[i], max_sides)
                    else:
                        continue
                if conditions.index("<") > conditions.index(">"):
                    if conditions[i] == ">":
                        conditionArguments[i] = sysr.randint(1, max_sides-1)
                    elif conditions[i] == "<":
                        conditionArguments[i] = sysr.randint(min_sides, conditionArguments[i])
                    else:
                        continue
            if "<" in conditions and ">" not in conditions:
                conditionArguments[i] = sysr.randint(2, max_sides)
            if ">" in conditions and "<" not in conditions:
                conditionArguments[i] = sysr.randint(1, max_sides-1)
        values = list(range(1,max_sides))
        for i in range(len(conditions)):
            if conditions[i] == "<":
                for j in range(1,conditionArguments[i]):
                    if j in values:
                        values.remove(j)
            elif conditions[i] == ">":
                for j in range(conditionArguments[i], max_sides):
                    if j in values:
                        values.remove(j)
            elif conditions[i] == "":
                values.remove(conditionArguments[i])
        aux = []
        for i in range(maxConditions):
            aux.append(conditions[i])
            aux.append(conditionArguments[i])
        out += "{"
        for i in range(len(aux)):
            out += aux[i]
            if i>0 and i%2 == 1:
                out += ","
        return out
def generateXdY(min_sides:int, max_sides:int, min_dice:int, max_dice:int, usecustomDice:bool=False, advanced:bool=False, allowSubExpressions:bool=False, allowZero:bool=False, allowNegativeValues:bool=False, maxConditions:int=4):
    if not advanced:
        if not usecustomDice:
            diceTemplate=generateDice(min_sides, max_sides)
            return sysr.randint(min_dice, max_dice)+diceTemplate
        else:
            if not allowZero and not allowNegativeValues:
                diceTemplate=generateDice(min_sides,max_sides, True, min_sides, max_sides)
            if allowZero and not allowNegativeValues:
                diceTemplate=generateDice(min_sides,max_sides, True, 0, max_sides)
            if not allowZero and allowNegativeValues:
                diceTemplate=generateDice(min_sides,max_sides, True, min_sides, max_sides, allowNegativeValuesWithoutZero=True)
            if allowZero and allowNegativeValues:
                diceTemplate=generateDice(min_sides,max_sides, True, -max_sides, max_sides)
            return sysr.randint(min_dice, max_dice)+diceTemplate
    else:
        if not usecustomDice:
            diceTemplate=generateDice(min_sides, max_sides)
            diceString = str(sysr.randint(min_dice, max_dice))+diceTemplate
            choice1 = sysr.choice(["keep","drop"])
            if choice1 == "keep":
                choice2 = sysr.choice(["lowest","middle","highest"])
                if choice2 == "lowest":
                    keepLowest = sysr.randint(1,max_dice-1)
                    if keepLowest == 1:
                        diceString += "KL"
                    else:
                        diceString += "KL" + str(keepLowest)
                if choice2 == "middle":
                    keepMiddle = sysr.randint(1,max_dice-1)
                    if keepMiddle == 1:
                        diceString += "KM"
                    else:
                        diceString += "KM" + str(keepMiddle)
                if choice2 == "highest":
                    keepHighest = sysr.randint(1,max_dice-1)
                    if keepHighest == 1:
                        diceString += "KH"
                    else:
                        diceString += "KH" + str(keepHighest)
            if choice1 == "drop":
                choice2 == sysr.choice(["lowest", "highest", "condition"])
                if choice2 == "lowest":
                    dropLowest = sysr.randint(1,max_dice-1)
                    if dropLowest == 1:
                        diceString += "DL"
                    else:
                        diceString += "DL" + str(dropLowest)
                if choice2 == "highest":
                    dropHighest = sysr.randint(1,max_dice-1)
                    if dropHighest == 1:
                        diceString += "DH"
                    else:
                        diceString += "DH" + str(dropHighest)
                # Drop Conditions in Sophie's dice are parsed as an OR, not an AND Like the default for literally everything else
                if choice2 == "condition":
                    diceString += conditionHelper(maxConditions, min_sides, max_sides, allowZero, allowNegativeValues)