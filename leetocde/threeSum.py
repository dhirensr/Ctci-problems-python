def threeSum(nums):
    nums.sort()
    n=len(nums)
    s=set()
    for i in range(n):
        j=i+1
        k=n-1
        while(j<k):
            c=nums[i]+nums[j]+nums[k]
            if c==0:
                s.add((nums[i],nums[j],nums[k]))
            if c<=0:
                j+=1
            else:
                k-=1
    return list(map(list,s))
