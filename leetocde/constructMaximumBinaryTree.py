
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def constructMaximumBinaryTree(nums):
    """
    https://leetcode.com/problems/maximum-binary-tree/
    """
    if len(nums)==0:
        return None
    index= nums.index(max(nums))
    root = TreeNode(nums[index])
    left_array = nums[:index]
    right_array = nums[index+1:]
    root.left = constructMaximumBinaryTree(left_array)
    root.right = constructMaximumBinaryTree(right_array)
    return root

print(constructMaximumBinaryTree([3,2,1,6,0,5]))
