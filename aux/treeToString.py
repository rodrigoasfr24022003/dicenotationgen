from classes.BinaryTree import BinaryTree
def treeToString(tree: BinaryTree, result: list):

    if tree is None:
        return
    
    result.append(str(tree.data))

    if not tree.left or tree.right:
        return
    
    result.append("(")
    treeToString(tree.left, result)
    result.append(')')

    if tree.right:
        result.append("(")
        treeToString(tree.left, result)
        result.append(")")
def stringHelper(tree):
    result = []
    treeToString(tree, result)
    print("".join(result))