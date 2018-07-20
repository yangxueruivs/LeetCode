class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        elif len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])
        
        maj1, maj2, maj3 = nums[0], nums[1], nums[2] + nums[0]
        for i in range(3, len(nums)):
            temp3, temp2 = maj3, maj2
            maj3 = max((maj1 + nums[i]), (maj2 + nums[i]))
            maj2 = temp3
            maj1 = temp2
            
        return max(maj1, maj2, maj3)
        