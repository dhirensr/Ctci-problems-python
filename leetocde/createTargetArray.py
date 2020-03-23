def createTargetArray(nums, index):
    """
    https://leetcode.com/problems/create-target-array-in-the-given-order/
    """
    target = []
    for num,idx in zip(nums,index):
        target = target[:idx] + [num,] + target[idx:]
    return target

print(createTargetArray([0,1,2,3,4],[0,1,2,2,1]))
