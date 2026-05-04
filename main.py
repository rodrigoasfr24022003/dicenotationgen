from aux.treeToString import stringHelper, treeToString
from generators.expression import generateExpression

print(stringHelper(treeToString(generateExpression(1,36,1,36))))