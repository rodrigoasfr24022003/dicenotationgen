from classes.BinaryTree import BinaryTree
from generators.dicenotationelement import generateXdY
import random
sysr = random.SystemRandom()
def generateExpression(min_sides:int, max_sides:int, min_dice:int, max_dice:int, usecustomDice:bool=False, advanced:bool=False, allowSubExpressions:bool=False, allowZero:bool=False, allowNegativeValues:bool=False, maxConditions:int=4, diceLadder:str="Evens", minExplosionLimit:int = 1, maxExplosionLimit:int = 6, treeDepth:int=4):
    tree = BinaryTree()
    binaryOperators = ["+","-","*","/","^"]
    if treeDepth == 0:
        tree.data = generateXdY(min_sides, max_sides, min_dice, max_dice, usecustomDice, advanced, allowSubExpressions, allowZero, allowNegativeValues, maxConditions, diceLadder, minExplosionLimit, maxExplosionLimit)
        return tree
    is_operator = sysr.choice([True,False])
    if is_operator:
        tree.data = sysr.choice(binaryOperators)
        tree.left = generateExpression(min_sides, max_sides, min_dice, max_dice, usecustomDice, advanced, allowSubExpressions, allowZero, allowNegativeValues, maxConditions, diceLadder, minExplosionLimit, maxExplosionLimit, treeDepth-1)
        tree.right = generateExpression(min_sides, max_sides, min_dice, max_dice, usecustomDice, advanced, allowSubExpressions, allowZero, allowNegativeValues, maxConditions, diceLadder, minExplosionLimit, maxExplosionLimit, treeDepth-1)
    else:
        tree.data = generateXdY(min_sides, max_sides, min_dice, max_dice, usecustomDice, advanced, allowSubExpressions, allowZero, allowNegativeValues, maxConditions, diceLadder, minExplosionLimit, maxExplosionLimit)
    return tree