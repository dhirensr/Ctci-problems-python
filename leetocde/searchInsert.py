def searchInsert(nums,target):
    low =0
    high = len(nums)-1
    end = True
    while end:
        mid = (low+high)//2
        if nums[mid] == target:
            end = False
            return mid
        if target > nums[mid]:
            low = mid+1
        if target < nums[mid]:
            high = mid-1
        if mid == low or high < low:
            end = False
)


    if target < nums[0]:
        return 0
    elif target > nums[-1]:
        return len(nums)
    for i in range(len(nums)-1):
        if nums[i] < target < nums[i+1]:
            return i+1

print(searchInsert([2,5],1))
