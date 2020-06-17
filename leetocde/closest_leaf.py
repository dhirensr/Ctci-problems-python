class newNode:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

def helper_distance(node,distance):
    if not (node.left and node.right):
        return distance
    left_dist = helper_distance(node.left,distance+1)
    right_dist = helper_distance(node.right,distance+1)
    return min(left_dist,right_dist)

def closest_leaf(node):
    if not (node.left and node.right):
        return 0
    return helper_distance(node,0)


root = newNode(1)
root.left = newNode(12)
root.right = newNode(13)
root.right.left = newNode(14)

root.right.left.left = newNode(21)
root.right.left.right = newNode(22)
x=root.right
print("The closest leaf to the node with value",
      x.key, "is at a distance of",
      closest_leaf(root))
