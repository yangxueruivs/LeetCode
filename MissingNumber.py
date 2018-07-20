class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        nums = sorted(nums)
        for i in range(len(nums)):
            if i != nums[i]:
                return i
            
        return len(nums)