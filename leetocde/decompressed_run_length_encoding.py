class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(0,len(nums),2):
            temp=[nums[i+1]]*nums[i]
            result+=temp
        return result
