#dp
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, n = nums[:], len(nums)
        out = res[0]
        for i in range(1,n):
            res[i] = max(res[i-1]+nums[i],nums[i])
            if res[i] > out:
                out = res[i]
        return out
#Divide&conquer nlogn