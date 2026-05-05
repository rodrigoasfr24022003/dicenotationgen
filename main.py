from generators.expression import generateExpression
import json
import random
sysr=random.SystemRandom()

presetName = input("Insert preset name here: ")

presetFile = open("presets/"+presetName+".json","r")

outFileName = input("Insert output file name here: ")

outFile = open("output/"+outFileName+".txt", "w")

amount = int(input("Insert expression amount here: "))

preset = json.load(presetFile)

# print(preset)

for i in range(amount-1):
    out = str(generateExpression(preset["min_sides"],preset["max_sides"],preset["min_dice_amount"],preset["max_dice_amount"],preset["min_number_amount"],preset["max_number_amount"],preset["custom_dice"],preset["advanced"],preset["allow_sub_expressions"],preset["allow_zero"],preset["allow_negative_values"],preset["max_conditions"],preset["dice_ladder"],preset["min_explosion_limit"],preset["max_explosion_limit"],sysr.randint(preset["min_tree_depth"],preset["max_tree_depth"])))
    outFile.write(out+'\n')
out = str(generateExpression(preset["min_sides"],preset["max_sides"],preset["min_dice_amount"],preset["max_dice_amount"],preset["min_number_amount"],preset["max_number_amount"],preset["custom_dice"],preset["advanced"],preset["allow_sub_expressions"],preset["allow_zero"],preset["allow_negative_values"],preset["max_conditions"],preset["dice_ladder"],preset["min_explosion_limit"],preset["max_explosion_limit"],sysr.randint(preset["min_tree_depth"],preset["max_tree_depth"])))
outFile.write(out)

presetFile.close()
outFile.close()