def smallerNumbersThanCurrent(nums):
    """
    https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
    """
    output = [0 for i in range(len(nums))]
    count =[0 for i in range(101)]
    for i in nums:
        count[i]+=1
    for idx,i in enumerate(nums):
        counter= 0
        for j in count[:i]:
            counter+=j
        output[idx] = counter
    return output

print(smallerNumbersThanCurrent([7,7,7,7]))
