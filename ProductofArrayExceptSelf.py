class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res, temp1, temp2 = [1], 1, 1
        for i in range(len(nums)-1):
            temp1 *= nums[i]
            res += [temp1]
            
        for i in range(len(nums)-1, -1, -1):
            res[i] *= temp2
            temp2 *= nums[i]
            
        return res