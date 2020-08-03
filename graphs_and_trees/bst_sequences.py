bst_sequences = []
def helper(node):
    if not node:
        return []
    if node.left == None and node.right==None:
        return [node.val]
    left_sequence = helper(node.left)
    right_sequence = helper(node.right)
    print([node.val]+left_sequence,[node.val]+right_sequence)





def bst_sequences(root):
    pass
