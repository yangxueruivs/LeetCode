class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        #print set(nums)
        nums[:] = sorted(list((set(nums))))
        return len(nums)