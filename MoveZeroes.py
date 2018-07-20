class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        
        i, count = 0, 0
        while i < len(nums) - count:
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)
                count += 1
                continue
            i += 1