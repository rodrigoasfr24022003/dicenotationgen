from generators.dicegen import generateDice
import random
sysr = random.SystemRandom()
def conditionHelper(startString:str,maxConditions:int, dice_sides:int, allow_zero:bool=False, allowNegativeValues:bool=False, useBrackets:bool=True, useCommas:bool=True, noEquality:bool=False):
    out = startString
    conditionAmount = sysr.randint(1,min(dice_sides,maxConditions))
    if not noEquality:
        if conditionAmount == 1:
            condition = sysr.choice(["<",">",""])
            if condition == "<":
                conditionArgument = sysr.randint(2 if not allow_zero else 1, dice_sides) if not allowNegativeValues else sysr.randint(-dice_sides+1, dice_sides) if allow_zero else sysr.choice(list(range(-dice_sides+1, dice_sides)).remove(0))
            elif condition == ">":
                conditionArgument = sysr.randint(1 if not allow_zero else 0, dice_sides-1) if not allowNegativeValues else sysr.randint(-dice_sides, dice_sides-1) if allow_zero else sysr.choice(list(range(-dice_sides, dice_sides-1)).remove(0))
            elif condition == "":
                conditionArgument = sysr.randint(1 if not allow_zero else 0, dice_sides) if not allowNegativeValues else sysr.randint(-dice_sides, dice_sides) if allow_zero else sysr.choice(list(range(-dice_sides, dice_sides)).remove(0))
            return "{" + str(condition) + str(conditionArgument) + "}"
        elif conditionAmount == 2:
            condition1 = sysr.choice(["<",">",""])
            if condition1 == "<":
                condition1Argument = sysr.randint(2, dice_sides)
                condition2 = sysr.choice([">", ""])
                valid_args = [x for x in range(condition1Argument + 1, dice_sides + 1)] if condition2 == "" else [x for x in range(condition1Argument + 1, dice_sides)]
                if valid_args:
                    condition2Argument = sysr.choice(valid_args)
                else:
                    condition2Argument = ""
            elif condition1 == ">":
                condition1Argument = sysr.randint(1, dice_sides-1)
                condition2 = sysr.choice(["<", ""])
                valid_args = [x for x in range(1, condition1Argument)] if condition2 == "" else [x for x in range(2, condition1Argument)]
                if valid_args:
                    condition2Argument = sysr.choice(valid_args)
                else:
                    condition2Argument = ""
            elif condition1 == "":
                condition1Argument = sysr.randint(1, dice_sides)
                condition2 = sysr.choice(["<",">",""])
                if condition2 == "<":
                    valid_args = [x for x in range(2, dice_sides + 1) if x != condition1Argument]
                    if valid_args:
                        condition2Argument = sysr.choice(valid_args)
                    else:
                        condition2Argument = ""
                if condition2 == ">":
                    valid_args = [x for x in range(1, dice_sides) if x != condition1Argument]
                    if valid_args:
                        condition2Argument = sysr.choice(valid_args)
                    else:
                        condition2Argument = ""
                if condition2 == "":
                    valid_args = [x for x in range(1, dice_sides + 1) if x != condition1Argument]
                    if valid_args:
                        condition2Argument = sysr.choice(valid_args)
                    else:
                        condition2Argument = ""
            return "{" + str(condition1) + str(condition1Argument) + "," + str(condition2) + str(condition2Argument) + "}"
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
                            conditionArguments[i] = sysr.randint(2 if not allow_zero else 1, dice_sides) if not allowNegativeValues else sysr.randint(-dice_sides+1, dice_sides) if allow_zero else sysr.choice(list(range(-dice_sides+1, dice_sides)).remove(0))
                        elif conditions[i] == ">":
                            conditionArguments[i] = sysr.randint(conditionArguments[i], dice_sides) if conditionArguments[i] <= dice_sides else dice_sides
                        else:
                            continue
                    if conditions.index("<") > conditions.index(">"):
                        if conditions[i] == ">":
                            conditionArguments[i] = sysr.randint(1 if not allow_zero else 0, dice_sides-1) if not allowNegativeValues else sysr.randint(-dice_sides, dice_sides-1) if allow_zero else sysr.choice(list(range(-dice_sides, dice_sides-1)).remove(0))
                        elif conditions[i] == "<":
                            conditionArguments[i] = sysr.randint(1, conditionArguments[i]) if conditionArguments[i] >= 2 else 1
                        else:
                            continue
                if "<" in conditions and ">" not in conditions:
                    conditionArguments[i] = sysr.randint(2 if not allow_zero else 1, dice_sides) if not allowNegativeValues else sysr.randint(-dice_sides+1, dice_sides) if allow_zero else sysr.choice(list(range(-dice_sides+1, dice_sides)).remove(0))
                if ">" in conditions and "<" not in conditions:
                    conditionArguments[i] = sysr.randint(1 if not allow_zero else 0, dice_sides-1) if not allowNegativeValues else sysr.randint(-dice_sides, dice_sides-1) if allow_zero else sysr.choice(list(range(-dice_sides, dice_sides-1)).remove(0))
        if noEquality:
            conditionAmount = sysr.randint(1,2)
            if conditionAmount == 1:
                condition = sysr.choice(["<",">"])
                if condition == "<":
                    conditionArgument = sysr.randint(2 if not allow_zero else 1, dice_sides) if not allowNegativeValues else sysr.randint(-dice_sides+1, dice_sides) if allow_zero else sysr.choice(list(range(-dice_sides+1, dice_sides)).remove(0))
                elif condition == ">":
                    conditionArgument = sysr.randint(1 if not allow_zero else 0, dice_sides-1) if not allowNegativeValues else sysr.randint(-dice_sides, dice_sides-1) if allow_zero else sysr.choice(list(range(-dice_sides, dice_sides-1)).remove(0))
                return "{" + str(condition) + str(conditionArgument) + "}"
            elif conditionAmount == 2:
                condition1 = sysr.choice(["<",">"])
                if condition1 == "<":
                    condition1Argument = sysr.randint(2 if not allow_zero else 1, dice_sides) if not allowNegativeValues else sysr.randint(-dice_sides+1, dice_sides) if allow_zero else sysr.choice(list(range(-dice_sides+1, dice_sides)).remove(0))
                    condition2 = ">"
                    condition2Argument = sysr.randint(condition1Argument, dice_sides-1)
                elif condition1 == ">":
                    condition1Argument = sysr.randint(1 if not allow_zero else 0, dice_sides-1) if not allowNegativeValues else sysr.randint(-dice_sides, dice_sides-1) if allow_zero else sysr.choice(list(range(-dice_sides, dice_sides-1)).remove(0))
                    condition2 = "<"
                    condition2Argument = sysr.randint(1,condition1Argument)
                return "{" + str(condition1) + str(condition1Argument) + "," + str(condition2) + str(condition2Argument) + "}"
        if not allowNegativeValues:
            values = list(range(1 if (not allow_zero) else 0,dice_sides))
        if allowNegativeValues and not allow_zero:
            values = list(range(-dice_sides,dice_sides)).remove(0)
        if allowNegativeValues and allow_zero:
            values = list(range(-dice_sides,dice_sides))
        if conditionAmount > 2:
            for i in range(len(conditions)):
                if conditions[i] == "<":
                    for j in range(1,conditionArguments[i]):
                        if j in values:
                            values.remove(j)
                elif conditions[i] == ">":
                    for j in range(conditionArguments[i], dice_sides):
                        if j in values:
                            values.remove(j)
                elif conditions[i] == "" and conditionArguments[i] in values:
                    values.remove(conditionArguments[i])
            aux = []
            for i in range(min(len(conditions), len(conditionArguments))):
                aux.append(conditions[i])
                aux.append(conditionArguments[i])
            out += "{" if useBrackets else ""
            for i in range(len(aux)):
                out += str(aux[i])
                if i>0 and i%2 == 1 and i<len(aux)-1 and useCommas:
                    out += ","
            out += "}" if useBrackets else ""
            return out
def generateXdY(min_sides:int, max_sides:int, min_dice:int, max_dice:int, usecustomDice:bool=False, advanced:bool=False, allowSubExpressions:bool=False, allowZero:bool=False, allowNegativeValues:bool=False, maxConditions:int=4, diceLadder:str="Evens", minExplosionLimit:int = 1, maxExplosionLimit:int = 6):
    if allowSubExpressions:
        raise NotImplementedError("Code for subexpression generation not implemented yet")
    if not advanced:
        if not usecustomDice:
            diceTemplate=generateDice(min_sides, max_sides)
            return str(sysr.randint(min_dice, max_dice))+diceTemplate
        else:
            if not allowZero and not allowNegativeValues:
                diceTemplate=generateDice(min_sides,max_sides, True, min_sides, max_sides)
            if allowZero and not allowNegativeValues:
                diceTemplate=generateDice(min_sides,max_sides, True, 0, max_sides)
            if not allowZero and allowNegativeValues:
                diceTemplate=generateDice(min_sides,max_sides, True, min_sides, max_sides, allowNegativeValuesWithoutZero=True)
            if allowZero and allowNegativeValues:
                diceTemplate=generateDice(min_sides,max_sides, True, -max_sides, max_sides)
            return str(sysr.randint(min_dice, max_dice))+diceTemplate
    else:
        if not usecustomDice:
            dice = generateDice(min_sides, max_sides)
            diceTemplate = dice[0]
            diceSides = dice[1]
            diceAmount = sysr.randint(min_dice, max_dice)
            diceString = str(diceAmount)+diceTemplate
            diceMorphemes = []
            diceMorphemes.append(diceString)
            choice1 = sysr.choice(["nothing","keep","drop"])
            if choice1 == "keep":
                choice2 = sysr.choice(["lowest","middle","highest"])
                if choice2 == "lowest":
                    keepLowest = sysr.randint(1,max_dice-1)
                    if keepLowest == 1:
                        diceMorphemes.append("KL")
                    else:
                        diceMorphemes.append("KL" + str(keepLowest))
                if choice2 == "middle":
                    keepMiddle = sysr.randint(1,max_dice-1)
                    if keepMiddle == 1:
                        diceMorphemes.append("KM")
                    else:
                        diceMorphemes.append("KM" + str(keepMiddle))
                if choice2 == "highest":
                    keepHighest = sysr.randint(1,max_dice-1)
                    if keepHighest == 1:
                        diceMorphemes.append("KH")
                    else:
                        diceMorphemes.append("KH" + str(keepHighest))
            if choice1 == "drop":
                choice2 = sysr.choice(["lowest", "highest", "condition"])
                if choice2 == "lowest":
                    dropLowest = sysr.randint(1,max_dice-1)
                    if dropLowest == 1:
                        diceMorphemes.append("DL")
                    else:
                        diceMorphemes.append("DL" + str(dropLowest))
                if choice2 == "highest":
                    dropHighest = sysr.randint(1,max_dice-1)
                    if dropHighest == 1:
                        diceMorphemes.append("DH")
                    else:
                        diceMorphemes.append("DH" + str(dropHighest))
                # Drop Conditions in Sophie's dice are parsed as an OR, not an AND Like the default for literally everything else
                if choice2 == "condition" and diceSides >=2:
                    diceMorphemes.append(conditionHelper("D", maxConditions, diceSides, allowZero, allowNegativeValues))
            choice3 = sysr.choice(["clamp", "noclamp"])
            if choice3 == "clamp":
                diceMorphemes.append( conditionHelper("C", maxConditions, diceSides, allowZero, allowNegativeValues, False, False, True) )
            if diceAmount <= max_sides-min_sides:
                choice4 = sysr.choices(["unique","non-unique"],weights=[0.1,0.9],k=1)[0]
            else:
                choice4 = "non-unique"
            if choice4 == "unique":
                diceMorphemes.append("U")
            choice5 = sysr.choice(["calm", "explosive", "inflating", "reducing"])
            isDisregarding = sysr.choices([True, False],weights=[0.1,0.9],k=1)[0]
            #no pattern support yet
            explosionSubmorphemes = []
            if choice5 == "explosive":
                explosionSubmorphemes.append("!")
                choice6 = sysr.choice(["conditional", "unconditional"])
                if choice6 == "conditional":
                    explosionSubmorphemes.append(conditionHelper("", maxConditions, diceSides, allowZero, allowNegativeValues))
                isLimited = sysr.choices([True, False],weights=[0.1,0.9],k=1)[0]
                if isLimited:
                    explosionSubmorphemes.append(str(sysr.randint(minExplosionLimit,maxExplosionLimit)))
            elif choice5 == "inflating":
                explosionSubmorphemes.append("!!")
                choice6 = sysr.choice(["conditional", "unconditional"])
                if choice6 == "conditional":
                    explosionSubmorphemes.append(conditionHelper("", maxConditions, diceSides, allowZero, allowNegativeValues))
            elif choice5 == "reducing":
                explosionSubmorphemes.append("!!!")
            if isDisregarding:
                explosionSubmorphemes.append(".")
            explosionString = ""
            for i in explosionSubmorphemes:
                explosionString += i
            diceMorphemes.append(explosionString)
            choice7 = sysr.choice(["","conditional","noReroll"])
            if choice7 == "":
                rerollStr = "R"
                isRerollLimited = sysr.choices([True, False],weights=[0.1,0.9],k=1)[0]
                if isRerollLimited:
                    rerollStr += str(sysr.randint(minExplosionLimit,maxExplosionLimit))
                diceMorphemes.append(rerollStr)
            elif choice7 == "conditional":
                rerollStr = conditionHelper("R", maxConditions, diceSides, allowZero, allowNegativeValues)
                isRerollLimited = sysr.choices([True, False],weights=[0.1,0.9],k=1)[0]
                if isRerollLimited:
                    rerollStr += str(sysr.randint(minExplosionLimit,maxExplosionLimit))
                diceMorphemes.append(rerollStr)
            choice8 = sysr.choice(["","conditional","noCount"])
            if choice8 == "":
                diceMorphemes.append("#")
            elif choice8 == "conditional":
                diceMorphemes.append(conditionHelper("#", maxConditions, diceSides, allowZero, allowNegativeValues))
            choice9 = sysr.choices(["","T","Ti","Tw","Twi"], k=1, weights=[1,0.1,0.1,0.1,0.01])[0]
            diceMorphemes.append(choice9)
            #multi-result support will be added later
            out = ""
            for i in diceMorphemes:
                out += str(i)
            return out
        else:
            raise NotImplementedError("Code for advanced custom dice not implemented yet")