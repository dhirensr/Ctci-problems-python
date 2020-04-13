def findMaxLength(nums):
    """
    https://leetcode.com/problems/contiguous-array/
    """
    cache = {}
    cache[0] = -1
    count = 0
    max_length =0
    for idx,i in enumerate(nums):
        if i==1:
            count = count + 1
        else:
            count -=1
        if count in cache:
            max_length = max(max_length,idx-cache[count])
        else:
            cache[count]= idx
    return max_length

findMaxLength([0,0,1,0,0,0,1,1])
