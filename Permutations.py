class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [nums]
        
        def subPermute(nums):
            if len(nums) == 1:
                    yield [nums[0]]
            else:
                for i in range(len(nums)):
                    for res in subPermute(nums[:i] + nums[i+1:]):
                        yield [nums[i]] + res
                
        return list(subPermute(nums))