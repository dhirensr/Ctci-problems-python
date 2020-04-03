def twoSum(nums,target):
    # if len(nums) ==2:
    #     return [0,1]
    # mid = (len(nums))//2
    # temp = nums.copy()
    # temp.sort()
    # if(temp[mid]< target):
    #     #left array search
    #     search_array = temp[mid:]
    # else:
    #     search_array = temp[:mid]
    # print(search_array)
    # result= []
    # for idx,i in enumerate(search_array):
    #     for j in search_array[idx:]:
    #         if(i+j== target):
    #             result.append(nums.index(i))
    #             result.append(nums.index(j))
    #             break
    # return result
    result = []
    for idx,i in enumerate(nums):
        if not result:
            if(target-i in nums[idx+1:]):
                result.append(nums.index(i))
                result.append(nums[idx+1:].index(target-i)+idx+1)
                break
    return result




print(twoSum([3,2,4],6))
