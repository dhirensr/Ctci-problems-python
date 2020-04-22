def subarraySum(nums,k):
    cache= {}
    sum=0
    count=0
    cache[0]=1
    for i in range(len(nums)):
        sum+=nums[i]
        sum_k= sum-k
        if sum_k in cache:
            count+=cache[sum_k]
        cache[sum]=cache.get(sum, 0) + 1
    return count
subarraySum([1,2,2,1,3],3)
